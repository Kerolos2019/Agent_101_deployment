from crewai import Agent, LLM
from config import settings


def build_search_queries_agent(llm: LLM) -> Agent:
    return Agent(
        role="Search Queries Recommendation Agent",
        goal="\n".join([
            "Provide a list of suggested search queries to be passed to the search engine.",
            "The queries must be varied and looking for specific items.",
        ]),
        backstory=(
            "The agent is designed to help in looking for products by providing "
            "a list of suggested search queries based on the context provided."
        ),
        llm=llm,
        verbose=True,
    )
