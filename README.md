# RPG Agents

A small D&D application built with Strands Agents. A Game Master orchestrator
uses two A2A agents—for rules and character management—and an MCP dice service.

## Setup

Install the dependencies from the repository root:

```bash
uv sync
```

Copy the environment template:

```bash
cp .env.example .env
```

All LLM configuration is read from `.env`. Set `LLM_PROVIDER` to switch every
agent between `ollama` and `bedrock`.

For local Ollama, install and start Ollama, pull a model that supports tool
calling, and configure it:

```dotenv
LLM_PROVIDER=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL_ID=qwen3:8b
```

For Amazon Bedrock, use either an AWS profile or AWS access keys in `.env`:

```dotenv
LLM_PROVIDER=bedrock
AWS_REGION=us-west-2
BEDROCK_MODEL_ID=global.anthropic.claude-sonnet-4-6
AWS_PROFILE=default
```

Alternatively, replace `AWS_PROFILE` with `AWS_ACCESS_KEY_ID`,
`AWS_SECRET_ACCESS_KEY`, and, when required, `AWS_SESSION_TOKEN`. Never commit
the `.env` file.

## Seed the rules database

The rules agent reads a local ChromaDB knowledge base backed by SQLite. Seed it
from the bundled D&D Basic Rules PDF before the first run:

```bash
cd 5_a2a_integration/utils
uv run python create_knowledge_base.py
cd ../..
```

This creates
`5_a2a_integration/utils/dnd_knowledge_base/chroma.sqlite3`. The generated
database is ignored by Git and can be rebuilt with the same command.

Character data is stored separately by TinyDB in
`5_a2a_integration/agents/character_agent/characters.json`; it does not require
SQLite seeding.

## Run the application

Open four terminals from the repository root and run one service in each.

Terminal 1 — dice roll MCP service (`:8080`):

```bash
cd 4_mcp_integration
uv run python dice_roll_mcp_server.py
```

Terminal 2 — rules A2A agent (`:8000`):

```bash
cd 5_a2a_integration/agents/rules_agent
uv run python rules_agent.py
```

Terminal 3 — character A2A agent (`:8001`):

```bash
cd 5_a2a_integration/agents/character_agent
uv run python character_agent.py
```

Terminal 4 — Game Master orchestrator API (`:8009`):

```bash
cd 5_a2a_integration/agents/gamemaster_orchestrator
uv run python gamemaster_orchestrator.py
```

Send a game request to the orchestrator:

```bash
curl -X POST http://localhost:8009/inquire \
  -H 'Content-Type: application/json' \
  -d '{"question":"Start a short adventure for a new character."}'
```

## Client UI

The UI is maintained separately on the
[`client`](https://github.com/regisfaria/rpg-agents/tree/client) branch.

The known-stable agent implementation is available on the
[`stable-v1`](https://github.com/regisfaria/rpg-agents/tree/stable-v1) branch.
