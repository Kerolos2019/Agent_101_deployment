from crewai import Agent, LLM


def build_report_agent(llm: LLM) -> Agent:
    return Agent(
        role="Procurement Report Author Agent",
        goal="Generate a professional HTML procurement report using Bootstrap.",
        backstory=(
            "The agent is designed to assist in generating a professional HTML "
            "procurement report after analysing a list of compared products."
        ),
        llm=llm,
        verbose=True,
    )
