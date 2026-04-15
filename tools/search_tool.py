from crewai.tools import tool
from tavily import TavilyClient
from config import settings

_client: TavilyClient | None = None


def _get_client() -> TavilyClient:
    global _client
    if _client is None:
        _client = TavilyClient(api_key=settings.TAVILY_API_KEY)
    return _client


@tool
def search_engine_tool(query: str) -> dict:
    """Search the web for current information about a query.

    Use this to find product pages, prices, or any web content.
    Returns a list of results with titles, URLs, content, and relevance scores.
    """
    return _get_client().search(query)
