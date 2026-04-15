from crewai import Agent, LLM
from tools import search_engine_tool


def build_search_engine_agent(llm: LLM) -> Agent:
    return Agent(
        role="Search Engine Agent",
        goal="Search for products based on the suggested search queries.",
        backstory=(
            "The agent is designed to help in looking for products by searching "
            "based on the suggested search queries and returning relevant results."
        ),
        llm=llm,
        verbose=True,
        tools=[search_engine_tool],
    )
