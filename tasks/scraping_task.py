import os
from crewai import Task, Agent
from models.schemas import AllExtractedProducts


def build_scraping_task(agent: Agent, output_dir: str) -> Task:
    return Task(
        description="\n".join([
            "Extract product details from e-commerce product page URLs.",
            "Collect results from multiple page URLs.",
            "Pick the best {top_recommendations_no} products from the search results.",
            "IMPORTANT: Only include products that are currently IN STOCK and available to purchase.",
            "If a product page shows 'out of stock', 'unavailable', 'discontinued', or no add-to-cart option, skip it entirely.",
            "Set in_stock=true only when the product can be ordered right now.",
        ]),
        expected_output="A JSON object containing product details.",
        output_json=AllExtractedProducts,
        output_file=os.path.join(output_dir, "step_3_scraped_products.json"),
        agent=agent,
    )
