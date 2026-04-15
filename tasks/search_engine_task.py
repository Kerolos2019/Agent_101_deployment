import os
from crewai import Task, Agent
from models.schemas import AllSearchResults


def build_search_engine_task(agent: Agent, output_dir: str) -> Task:
    return Task(
        description="\n".join([
            "Search for products based on all of the suggested search queries.",
            "Collect results from multiple queries.",
            "Ignore suspicious links or non-e-commerce single-product pages.",
            "Ignore search results with a confidence score below {score_th}.",
            "Results will be used to compare prices across different websites.",
        ]),
        expected_output="A JSON object containing the search results.",
        output_json=AllSearchResults,
        output_file=os.path.join(output_dir, "step_2_search_results.json"),
        agent=agent,
    )
