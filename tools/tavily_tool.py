from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key= os.getenv("TAVILY_API_KEY")
)


if not os.getenv("TAVILY_API_KEY"):
      raise RuntimeError("TAVILY_API_KEY not set in environment")

def tavily_search(query):
    try:
        response = client.search(query=query, max_results=5)
    except Exception as e:
        return f"Search failed: {e}"

    if not response.get("results"):
        return "No results found."

    results = []
    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()

        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)