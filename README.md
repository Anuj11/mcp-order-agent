# MCP Order Agent — Demo Project

A small educational example showing how a Python MCP server can expose an order lookup tool and how a LangChain agent can discover and use that tool.

## Project structure

- `server.py` — exposes `get_order_status` as an MCP tool.
- `agent.py` — connects to the local MCP server, discovers tools, and invokes a LangChain agent.
- `.env.example` — environment-variable template.
- `requirements.txt` — Python dependencies.

## Requirements

- Python 3.10+ (use a Python version supported by the current package releases)
- An API key for the configured model provider
- Internet access for installing packages and model API calls

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set `OPENAI_API_KEY` and `MODEL_NAME` to a model identifier supported by your installed LangChain integration.

Run the demo:

```bash
python agent.py
```

Test the missing-order path by changing `DEMO_ORDER_ID=9999` in `.env`.

## Important notes

- This is a demo with mock data, not a production order service.
- Package APIs and model identifiers can change. Before recording or sharing a tutorial, install the dependencies in a fresh virtual environment and test the complete flow with the package versions available at that time.
- Never commit `.env` or expose API keys in screen recordings.
- A production implementation needs customer-level authorization, tenant isolation, validation, timeouts, logging, tests, and secure access to the real order service.
- The demo uses local `stdio` transport. Do not print unrelated debug messages to standard output in an MCP server using `stdio`, because that stream is used by the protocol.

## Suggested test cases

1. `DEMO_ORDER_ID=1024` — expected to return a shipped order.
2. `DEMO_ORDER_ID=1025` — expected to return an order in processing.
3. `DEMO_ORDER_ID=9999` — expected to report that the order was not found.
