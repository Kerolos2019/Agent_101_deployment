from crewai import Agent, LLM
from tools import web_scraping_tool


def build_scraping_agent(llm: LLM) -> Agent:
    return Agent(
        role="Web Scraping Agent",
        goal="Extract product details from e-commerce page URLs.",
        backstory=(
            "The agent is designed to extract structured product information "
            "from any e-commerce URL. These details are used to compare products "
            "and decide which is the best to buy."
        ),
        llm=llm,
        tools=[web_scraping_tool],
        verbose=True,
    )
