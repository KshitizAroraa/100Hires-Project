# Collection Log

## YouTube Transcripts — Nathan Gotch

- **Tool:** Supadata API (https://supadata.ai)
- **Method:** Automated via `collect_youtube_transcripts.py` (repo root)
- **API used:** YouTube Data API v3 (channel → uploads playlist → video list) + Supadata transcript API
- **Date collected:** 2026-07-04
- **Videos collected:** 100 transcripts from @nathangotch channel
- **Output format:** `<video-id>-<slug>.txt` with header block (title, video ID, published date, URL), then full transcript text
- **Environment variables required:** `YOUTUBE_API_KEY`, `SUPADATA_API_KEY`

## LinkedIn Posts — All Authors

- **Method:** Manual collection (LinkedIn does not offer a public API for post content)
- **Date collected:** 2026-07-04
- **Authors collected:** Kevin Indig (4 posts), Lily Ray (1 post), Rand Fishkin (3 posts), Mike King (3 posts), Aleyda Solis (3 posts), Marie Haynes (3 posts), Eli Schwartz (3 posts), Dan Petrovic (3 posts), Jake Ward (3 posts)
- **Total posts:** 26
- **Attribution:** Each file retains the original post URL where available
