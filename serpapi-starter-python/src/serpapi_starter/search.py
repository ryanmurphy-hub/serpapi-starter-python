import os
import requests

SERPAPI_URL = "https://serpapi.com/search.json"

class SerpApiClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI_API_KEY is not set")

    def google_search(self, q: str, **params) -> dict:
        payload = {"engine": "google", "q": q, "api_key": self.api_key, **params}
        r = requests.get(SERPAPI_URL, params=payload, timeout=30)
        r.raise_for_status()
        return r.json()
