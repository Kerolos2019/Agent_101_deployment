import os
from crewai import Crew, LLM, Process
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

from config import settings
from agents import (
    build_search_queries_agent,
    build_search_engine_agent,
    build_scraping_agent,
    build_report_agent,
)
from tasks import (
    build_search_queries_task,
    build_search_engine_task,
    build_scraping_task,
    build_report_task,
)


ABOUT_COMPANY = (
    "Rankyx is a company that provides AI solutions to help websites refine "
    "their search and recommendation systems."
)


def build_crew(output_dir: str | None = None) -> Crew:
    """Assemble the full CrewAI crew and return it ready to kickoff."""
    if output_dir is None:
        output_dir = settings.OUTPUT_DIR

    os.makedirs(output_dir, exist_ok=True)

    llm = LLM(
        model=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
    )

    # Agents
    sq_agent = build_search_queries_agent(llm)
    se_agent = build_search_engine_agent(llm)
    sc_agent = build_scraping_agent(llm)
    rp_agent = build_report_agent(llm)

    # Tasks
    sq_task = build_search_queries_task(sq_agent, output_dir)
    se_task = build_search_engine_task(se_agent, output_dir)
    sc_task = build_scraping_task(sc_agent, output_dir)
    rp_task = build_report_task(rp_agent, output_dir)

    company_context = StringKnowledgeSource(content=ABOUT_COMPANY)

    return Crew(
        agents=[sq_agent, se_agent, sc_agent, rp_agent],
        tasks=[sq_task, se_task, sc_task, rp_task],
        process=Process.sequential,
        knowledge_sources=[company_context],
    )
