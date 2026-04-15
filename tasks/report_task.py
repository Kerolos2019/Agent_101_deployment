import os
from crewai import Task, Agent


def build_report_task(agent: Agent, output_dir: str) -> Task:
    return Task(
        description="\n".join([
            "Generate a professional HTML procurement report.",
            "Use Bootstrap CSS framework for a polished UI.",
            "Use the provided company context to personalise the report.",
            "Include prices and product comparisons from different websites.",
            "Structure the report with these sections:",
            "1. Executive Summary",
            "2. Introduction",
            "3. Methodology",
            "4. Findings: detailed price comparison tables and charts",
            "5. Analysis: trends and key observations",
            "6. Recommendations",
            "7. Conclusion",
            "8. Appendices",
        ]),
        expected_output="A complete, self-contained HTML page for the procurement report.",
        output_file=os.path.join(output_dir, "step_4_procurement_report.html"),
        agent=agent,
    )
