# Daily LinkedIn Post Agent 🤖

An autonomous AI agent that scrapes daily AI/ML trends, generates context-aware LinkedIn posts using LLMs, and publishes them automatically — zero manual intervention.

## How It Works

```
Google News (AI/ML trends)
        ↓
Scraper fetches top headlines
        ↓
LLM generates a LinkedIn post (OpenRouter API)
        ↓
Buffer API publishes to LinkedIn
        ↓
GitHub Actions runs this automatically every day
```

## Features

- **Automated trend scraping** — fetches real-time AI/ML news via GNews
- **LLM-powered post generation** — context-aware, non-repetitive posts with history tracking
- **Auto-publishing** — posts directly to LinkedIn via Buffer API (GraphQL)
- **Cloud deployment** — runs on GitHub Actions cron schedule, no local setup needed
- **Post history** — tracks previous posts to avoid repetitive content

## Tech Stack

| Component | Technology |
|---|---|
| Trend Scraping | GNews (Google News) |
| Post Generation | OpenRouter API (Llama 3.3 70B) |
| LinkedIn Publishing | Buffer API (GraphQL) |
| Automation | GitHub Actions (cron) |
| Language | Python |

## Project Structure

```
├── scraper.py          # Fetches trending AI/ML topics from Google News
├── post_generator.py   # Generates LinkedIn post using LLM
├── linkedin_poster.py  # Publishes post via Buffer API
├── main.py             # Orchestrates the full pipeline
├── scheduler.py        # Local scheduling alternative
├── get_channel_id.py   # Utility to fetch Buffer channel ID
├── config.py           # Configuration and environment variables
├── post_history.json   # Tracks recent posts to avoid repetition
└── .github/
    └── workflows/
        └── daily_post.yml  # GitHub Actions workflow
```

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/SaniaKhizar/daily-linkedIn-post-agent.git
cd daily-linkedIn-post-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file:
```
OPENROUTER_API_KEY=your_key
BUFFER_API_KEY=your_key
CHANNEL_ID=your_linkedin_channel_id
```

### 4. Get your Buffer Channel ID
```bash
python get_channel_id.py
```

### 5. Run manually
```bash
python main.py
```

### 6. Deploy on GitHub Actions
Add these secrets to your GitHub repo:
- `OPENROUTER_API_KEY`
- `BUFFER_API_KEY`
- `CHANNEL_ID`

The workflow runs automatically on schedule (Mon, Wed, Fri).

## How Post Generation Works

1. Scraper fetches top 10 AI/ML headlines from Google News
2. Random hook style selected (statistic, opinion, question, story)
3. Last 5 posts loaded from history to avoid repetition
4. LLM generates a 150-200 word post from student perspective
5. Post saved to history and published via Buffer API


📂 [GitHub](https://github.com/SaniaKhizar) | 🔗 [LinkedIn](https://www.linkedin.com/in/sania-khizar-4296b3414)
