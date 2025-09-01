# SerpApi Starter Python

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub stars](https://img.shields.io/github/stars/ryanmurphy-hub/serpapi-starter-python?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/ryanmurphy-hub/serpapi-starter-python)
![Build](https://github.com/ryanmurphy-hub/serpapi-starter-python/actions/workflows/ci.yml/badge.svg)

Minimal Python starter with CI, tests, and examples.


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
