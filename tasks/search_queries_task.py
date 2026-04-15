import os
from crewai import Task, Agent
from models.schemas import SuggestedSearchQueries
from config import settings


def build_search_queries_task(agent: Agent, output_dir: str) -> Task:
    return Task(
        description="\n".join([
            "Rankyx is looking to buy {product_name} at the best prices (value-for-money strategy).",
            "The company targets any of these websites to buy from: {websites_list}.",
            "The company wants to reach all available products on the internet to compare later.",
            "The stores must sell the product in {country_name}.",
            "Generate at maximum {no_keywords} queries.",
            "The search keywords must be in {language} language.",
            "Keywords must contain specific brands, types, or technologies. Avoid generic keywords.",
            "Each query must lead to an e-commerce product page, not a blog or listing page.",
        ]),
        expected_output="A JSON object containing a list of suggested search queries.",
        output_json=SuggestedSearchQueries,
        output_file=os.path.join(output_dir, "step_1_suggested_search_queries.json"),
        agent=agent,
    )
