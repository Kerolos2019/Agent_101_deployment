from crewai.tools import tool
from scrapegraph_py import Client
from config import settings
from models.schemas import SingleExtractedProduct

_client: Client | None = None


def _get_client() -> Client:
    global _client
    if _client is None:
        _client = Client(api_key=settings.SCRAPEGRAPH_API_KEY)
    return _client


@tool
def web_scraping_tool(page_url: str) -> dict:
    """Scrape an e-commerce product page and extract structured product details.

    Extracts price, title, image, specs, and recommendation notes.

    Example:
        web_scraping_tool(page_url="https://www.noon.com/egypt-en/some-product")
    """
    details = _get_client().smartscraper(
        website_url=page_url,
        user_prompt=(
            "Extract ```json\n"
            + SingleExtractedProduct.schema_json()
            + "```\nFrom the web page"
        ),
    )
    return {"page_url": page_url, "details": details}
