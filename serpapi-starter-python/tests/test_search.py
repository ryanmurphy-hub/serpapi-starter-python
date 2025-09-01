from serpapi_starter.search import SerpApiClient
import pytest
import os

def test_env_required(monkeypatch):
    monkeypatch.delenv("SERPAPI_API_KEY", raising=False)
    with pytest.raises(ValueError):
        SerpApiClient()
