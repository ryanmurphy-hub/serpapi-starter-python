# SerpApi Starter (Python)

Tiny starter showing a clean layout, env-based auth, a basic search, and tests.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e . pytest requests
cp .env.example .env  # add your SERPAPI_API_KEY
```

## Run
```bash
python examples/basic_search.py
```

## Test
```bash
pytest
```
