from serpapi_starter.search import SerpApiClient

if __name__ == "__main__":
    client = SerpApiClient()
    data = client.google_search("site:serpapi.com serpapi")
    organic = data.get("organic_results", [])[:3]
    for i, item in enumerate(organic, 1):
        print(f"{i}. {item.get('title')} -> {item.get('link')}")
