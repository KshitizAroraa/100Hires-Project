import os
import re
import time
from pathlib import Path

import requests
from googleapiclient.discovery import build

CHANNEL_HANDLE = "@nathangotch"
OUTPUT_DIR = Path("research/youtube-transcripts/nathan-gotch")
SUPADATA_BASE_URL = "https://api.supadata.ai/v1"


def get_api_keys():
    youtube_key = os.environ.get("YOUTUBE_API_KEY")
    supadata_key = os.environ.get("SUPADATA_API_KEY")
    if not youtube_key:
        raise ValueError("YOUTUBE_API_KEY environment variable is not set")
    if not supadata_key:
        raise ValueError("SUPADATA_API_KEY environment variable is not set")
    return youtube_key, supadata_key


def resolve_channel_id(youtube, handle):
    clean_handle = handle.lstrip("@")
    response = (
        youtube.channels()
        .list(part="contentDetails,snippet", forHandle=clean_handle)
        .execute()
    )
    items = response.get("items", [])
    if not items:
        raise ValueError(f"No channel found for handle: {handle}")
    channel = items[0]
    return channel["id"], channel["contentDetails"]["relatedPlaylists"]["uploads"]


def list_channel_videos(youtube, uploads_playlist_id):
    videos = []
    page_token = None

    while True:
        response = (
            youtube.playlistItems()
            .list(
                part="snippet,contentDetails",
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=page_token,
            )
            .execute()
        )

        for item in response.get("items", []):
            snippet = item["snippet"]
            videos.append(
                {
                    "video_id": item["contentDetails"]["videoId"],
                    "title": snippet["title"],
                    "published_at": snippet.get("publishedAt", ""),
                }
            )

        page_token = response.get("nextPageToken")
        if not page_token:
            break

    return videos


def safe_filename(title):
    cleaned = re.sub(r"[^\w\s-]", "", title).strip().lower()
    cleaned = re.sub(r"[-\s]+", "-", cleaned)
    return cleaned[:80] or "untitled"


def fetch_transcript(video_id, supadata_key):
    url = f"https://www.youtube.com/watch?v={video_id}"
    headers = {"x-api-key": supadata_key}
    params = {"url": url, "text": "true", "mode": "auto"}

    response = requests.get(
        f"{SUPADATA_BASE_URL}/transcript", headers=headers, params=params, timeout=120
    )

    if response.status_code == 202:
        job_id = response.json().get("jobId")
        if not job_id:
            return None

        for _ in range(30):
            time.sleep(5)
            job_response = requests.get(
                f"{SUPADATA_BASE_URL}/transcript/{job_id}",
                headers=headers,
                timeout=60,
            )
            if job_response.status_code == 200:
                data = job_response.json()
                content = data.get("content")
                if isinstance(content, str):
                    return content
                if isinstance(content, list):
                    return "\n".join(chunk.get("text", "") for chunk in content)
            elif job_response.status_code not in (202, 404):
                job_response.raise_for_status()
        return None

    response.raise_for_status()
    data = response.json()
    content = data.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(chunk.get("text", "") for chunk in content)
    return None


def save_transcript(video, transcript_text):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{video['video_id']}-{safe_filename(video['title'])}.txt"
    output_path = OUTPUT_DIR / filename

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(f"Title: {video['title']}\n")
        file.write(f"Video ID: {video['video_id']}\n")
        file.write(f"Published: {video['published_at']}\n")
        file.write(f"URL: https://www.youtube.com/watch?v={video['video_id']}\n")
        file.write("\n---\n\n")
        file.write(transcript_text)

    return output_path


def main():
    youtube_key, supadata_key = get_api_keys()
    youtube = build("youtube", "v3", developerKey=youtube_key)

    print(f"Resolving channel handle: {CHANNEL_HANDLE}")
    channel_id, uploads_playlist_id = resolve_channel_id(youtube, CHANNEL_HANDLE)
    print(f"Channel ID: {channel_id}")

    videos = list_channel_videos(youtube, uploads_playlist_id)
    print(f"Found {len(videos)} videos")

    saved = 0
    skipped = 0

    for index, video in enumerate(videos, start=1):
        print(f"[{index}/{len(videos)}] Fetching transcript: {video['title']}")
        try:
            transcript = fetch_transcript(video["video_id"], supadata_key)
            if not transcript:
                print(f"  No transcript available for {video['video_id']}")
                skipped += 1
                continue

            output_path = save_transcript(video, transcript)
            print(f"  Saved: {output_path}")
            saved += 1
            time.sleep(1)
        except Exception as error:
            print(f"  Failed for {video['video_id']}: {error}")
            skipped += 1

    print(f"\nDone. Saved {saved} transcripts, skipped {skipped}.")


if __name__ == "__main__":
    main()
