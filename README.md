---
title: Tech Stack Advisor
emoji: 🧠
colorFrom: indigo
colorTo: pink
sdk: docker
app_file: app.py
pinned: false
license: apache-2.0
duplicable: true
---

# Procurement AI Agent

A multi-agent AI pipeline that automates product research and procurement decisions. Give it a product name and target websites — it searches, scrapes, ranks, and delivers a structured HTML report.

Built with **CrewAI**, **Streamlit**, **Tavily Search**, and **ScrapeGraph**.

---

## How It Works

Four specialized AI agents run sequentially:

```
User Input
    │
    ▼
[Agent 1] Search Queries Agent
    │  Generates varied search queries for the product
    ▼
[Agent 2] Search Engine Agent         (Tavily API)
    │  Runs queries, returns ranked URLs filtered by relevance score
    ▼
[Agent 3] Scraping Agent              (ScrapeGraph API)
    │  Visits each URL, extracts price, specs, discounts, images
    ▼
[Agent 4] Report Agent
    │  Ranks products, writes a downloadable HTML procurement report
    ▼
Output: JSON step artifacts + HTML report saved to ./output/
```

---

## Prerequisites

You will need API keys for:

| Service | Purpose | Get it at |
|---|---|---|
| OpenAI | LLM powering all agents (GPT-4o) | platform.openai.com |
| Tavily | Web search | app.tavily.com |
| ScrapeGraph | AI-powered scraping | scrapegraphai.com |
| AgentOps | Agent monitoring (optional) | app.agentops.ai |

---

## Setup

### 1. Clone and configure

```bash
git clone <repo-url>
cd agent_101

cp .env.example .env
# Edit .env and fill in your API keys
```

### 2. Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501`.

### 3. Run with Docker

```bash
docker compose up --build
```

Open `http://localhost:8501`. Results are saved to `./output/` on your host machine.

---

## Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | Yes | — | OpenAI API key |
| `TAVILY_API_KEY` | Yes | — | Tavily search API key |
| `SCRAPEGRAPH_API_KEY` | Yes | — | ScrapeGraph API key |
| `AGENTOPS_API_KEY` | No | — | AgentOps monitoring key |
| `LLM_MODEL` | No | `gpt-4o-mini` | OpenAI model to use |
| `LLM_TEMPERATURE` | No | `0` | LLM temperature (0 = deterministic) |
| `OUTPUT_DIR` | No | `./output` | Directory for saving artifacts |

---

## Using the App

1. Enter the **product** you want to research (e.g. `coffee machine for the office`)
2. List **target websites** (one per line, e.g. `www.amazon.eg`)
3. Set your **country** and **search language**
4. Adjust **max keywords**, **top results**, and **minimum relevance score**
5. Click **Run Agent** and wait a few minutes
6. View step-by-step results and download the HTML report

---

## Project Structure

```
agent_101/
├── app.py                  # Streamlit entry point
├── config/
│   └── settings.py         # Env var loading and validation
├── agents/                 # 4 CrewAI agent definitions
├── tasks/                  # 4 CrewAI task definitions
├── tools/
│   ├── search_tool.py      # Tavily search tool
│   └── scraping_tool.py    # ScrapeGraph scraping tool
├── models/
│   ├── crew.py             # Crew assembly
│   └── schemas.py          # Pydantic data models
├── controllers/
│   └── crew_controller.py  # Orchestrates run, exposes results
├── views/
│   ├── sidebar.py          # Streamlit sidebar form
│   └── results.py          # Streamlit results display
├── output/                 # Generated artifacts (git-ignored)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Deploy to Hugging Face Spaces

1. Create a new Space with **Docker** SDK at huggingface.co/new-space
2. Add your API keys under **Settings → Variables and secrets**
3. Push this repo to the Space:

```bash
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
git remote show
git remote show hf
git remote set-url hf https://kerolosyacoub:<YOUR_TOKEN>@huggingface.co/spaces/kerolosyacoub/agent_101
git push hf main --force

```

The app will be live at `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`.

> Note: The Dockerfile already uses port 7860 as required by Hugging Face Spaces.

---

## Output Files

After each run, the following files are saved to `./output/`:

| File | Contents |
|---|---|
| `step_1_suggested_search_queries.json` | Generated search queries |
| `step_2_search_results.json` | Ranked URLs from Tavily |
| `step_3_scraped_products.json` | Extracted product data |
| `step_4_procurement_report.html` | Final downloadable report |
