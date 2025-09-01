![Build](https://github.com/ryanmurphy-hub/serpapi-starter-python/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


# SerpApi Starter (Python)

This repository is a minimal, production-ready Python starter for working with [SerpApi](https://serpapi.com/).  
It demonstrates clean project structure, environment-based authentication, example usage, tests, and GitHub Actions CI.

---

## Features
- 🔑 API key authentication via `.env` file (handled by [python-dotenv](https://pypi.org/project/python-dotenv/))
- 📦 Organized Python package layout (`src/serpapi_starter`)
- 🧪 Basic unit test with `pytest`
- ⚙️ GitHub Actions workflow for CI
- 📖 Example script for quick search testing

---

## Setup

Clone the repository and create a virtual environment:

```powershell
git clone https://github.com/your-username/serpapi-starter-python.git
cd serpapi-starter-python
python -m venv .venv
.\.venv\Scripts\Activate.ps1
