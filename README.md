# Cursor Setup — 100Hires Project

This document describes how Cursor was installed and configured for this project, including the **Claude Code** and **Codex** add-on extensions.

## Overview

The following tools are installed and set up:

| Tool | Status |
|------|--------|
| **Cursor IDE** | Installed |
| **GitHub account** | Connected to Cursor |
| **Claude Code** extension | Installed |
| **Codex** extension | Installed and signed in |

---

## Installation & Setup Steps

### 1. Install Cursor

1. Go to [https://cursor.com](https://cursor.com) and download Cursor for macOS.
2. Open the downloaded installer (`.dmg`) and drag **Cursor** into the **Applications** folder.
3. Launch Cursor from Applications (or Spotlight).
4. Complete the initial onboarding prompts (theme, keybindings, etc.) if shown.

### 2. Connect GitHub to Cursor

A GitHub account was already available, so the next step was linking it to Cursor:

1. In Cursor, open **Settings** or the account/sign-in area (typically via the profile icon or onboarding screen).
2. Choose **Sign in with GitHub**.
3. Authorize Cursor in the browser when GitHub prompts for permissions.
4. Return to Cursor and confirm the GitHub account is connected.

This allows Cursor to access repositories, sync settings, and use GitHub-related features inside the editor.

### 3. Install Add-on Extensions

Two AI add-on extensions were installed from the Cursor/VS Code extensions marketplace:

#### Claude Code (Claude AI)

1. Open the **Extensions** panel (`Cmd + Shift + X`).
2. Search for **Claude Code** or **Claude AI**.
3. Click **Install** on the official Claude extension.
4. Reload Cursor.

#### Codex

1. In the **Extensions** panel, search for **Codex**.
2. Click **Install** on the Codex extension.
3. Reload Cursor.

### 4. Sign In to Codex

After installing the Codex extension:

1. Open the Codex panel or use the command palette (`Cmd + Shift + P`) and search for Codex-related sign-in commands.
2. Follow the sign-in flow for your Codex account (browser redirect or in-app authentication).
3. Confirm you are signed in before using Codex features in the editor.

---

## Issues Faced During Setup

The following issues were encountered while installing Cursor and configuring the GitHub connection, extensions, and Codex sign-in. 

### Extension installation

- I was unaware about the cursor reload required after installing the extension. After reloading the extension was available on the pallete


---

## Quick Reference

| Action | Shortcut / Location |
|--------|---------------------|
| Extensions panel | `Cmd + Shift + X` |
| Command palette | `Cmd + Shift + P` |
| Cursor website | [https://cursor.com](https://cursor.com) |

---
# AI-Powered SEO Content Production — Research Repository

## Project Description

This repository is a primary-source research base on **AI-powered SEO
content production** — how practitioners are actually using AI to plan,
write, and scale content that ranks and gets cited by both traditional
search engines and AI answer engines (Google AI Overviews, AI Mode,
ChatGPT, Perplexity).

The goal isn't to summarize what's already been written about this topic —
it's to collect real, dated, source-linked material (LinkedIn posts,
YouTube transcripts) directly from people who are shipping this work today,
so that material can later support an actual playbook grounded in what
practitioners are doing right now rather than recycled advice.

Every source in this repo was chosen and verified against three criteria,
not popularity:

1. **Recent activity** — active posting/publishing within the last 1–2 months
2. **Third-party corroboration** — referenced, cited, or sharing a stage
   with other recognized practitioners, not just self-promoted
3. **A specific, checkable claim** — a real number, named client, or named
   study backing their expertise, not vague authority

The full research and verification process — including two names that were
considered and deliberately set aside

## The 10 Creators

### Kevin Indig
Growth advisor who previously led SEO/Growth at Shopify, G2, and Atlassian.
Writes the *Growth Memo* newsletter (25K+ subscribers) and publishes
original research rather than recycled advice — e.g. quantifying that
44.2% of AI citations come from the first 30% of a page. Co-hosts a weekly
podcast with Eli Schwartz. Speaking at Kalicube Summit, June 2026.

### Lily Ray
VP of SEO Strategy & Research at Amsive. Tracks real algorithm-update
casualties with hard data (documented brands losing 29–49% of traffic to
specific spam updates) and runs live AMAs answering practitioner questions
directly. Confirmed speaker at SEO Week 2026.

### Rand Fishkin
Co-founder of SparkToro, former CEO of Moz. Publishes primary audience and
search-behavior research — most recently a June 2026 study finding 68.01%
of Google searches end without a click. His research has previously been
cited by the US DOJ, FTC, WSJ, and Washington Post.

### Mike King
Founder/CEO of iPullRank. Coined "Relevance Engineering" — using LLMs to
reverse-engineer what search and AI systems actually reward. Founded SEO
Week, a real practitioner conference (40+ speakers), and publishes
technical research with hard numbers (e.g. a May 2026 study on GPT-5.5
citation sourcing).

### Aleyda Solis
International SEO consultant at Orainti. Documented how AI systems
decompose queries into sub-queries ("query fan-out"), reshaping how
practitioners approach topical coverage. Hosts the weekly *Crawling
Mondays* podcast. Confirmed speaker at SEO Week 2026.

### Marie Haynes
Founder of Marie Haynes Consulting. Among the first to publicly document
Google's AI Mode query fan-out behavior. Runs a biweekly podcast (*Search
News You Can Use*) and newsletter, and was directly quoted by Search Engine
Journal on the May 2026 core update.

### Eli Schwartz
Growth advisor and author of *Product-Led SEO*. Built SEO programs from
near-zero at multiple named companies (WordPress, Coinbase, Shutterstock,
Zendesk, SurveyMonkey), giving his advice a track record across different
business models rather than a single case study. Active Substack (17K+
subscribers) through June 2026, co-hosts a weekly podcast with Kevin Indig.

### Dan Petrovic
Managing Director of DEJAN (Australia). Ran a large-scale empirical study —
7,060 real queries, 2,275 tokenized pages, 883,262 extracted grounding
snippets — to reverse-engineer Google's AI "grounding budget." His research
is independently cited by multiple unrelated SEO sources, not just his own
channels.

### Nathan Gotch
CEO of Rankability and Search OS. Runs an active YouTube channel (125K+
subscribers, 300+ videos) specifically on SEO and AI search systems across
Google, ChatGPT, and Perplexity. Verifiable client result: Zacc Dukowitz at
Flyability credits Gotch's systems for 59% YoY organic traffic growth
(262K → 417K visits). Note: an independent review flagged some
rebranding/buzzword-chasing criticism worth watching for when selecting
which of his content to pull.

### Jake Ward
Co-founder of Byword (an AI content production tool) and founder of
Content Growth. Publishes real programmatic-SEO case studies with hard
numbers — including building 13,000+ AI-generated pages in 3 hours and
documenting a 466% traffic increase in 60 days. Practices what he teaches:
Byword is the actual product he runs.

## Repo structure

```
research/
├── sources.md              # Full expert list, links, annotations, verification log
├── linkedin-posts/         # Manually collected posts, organized by author
├── youtube-transcripts/    # API-collected transcripts, organized by video
└── other/                  # Podcast notes, newsletter excerpts, etc.
```

## Methodology notes

- **YouTube transcripts** were collected via API rather than manual
  transcription (see `research/other/collection-log.md` for the exact
  method/tool used).
- **LinkedIn posts** were collected manually, since LinkedIn does not offer
  a public API for post content — each post retains its original URL and
  publish date for attribution.
- This repo is updated incrementally, with commits reflecting individual
  research sessions rather than one final dump — the commit history itself
  is part of the deliverable.


