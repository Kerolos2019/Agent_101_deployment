import os
import json
import agentops

from config import settings
from models import build_crew, CrewInputs


class CrewController:
    """Orchestrates the CrewAI run and exposes results to the view layer."""

    def __init__(self):
        self._agentops_initialised = False

    def _init_agentops(self) -> None:
        if self._agentops_initialised or not settings.AGENTOPS_API_KEY:
            return
        agentops.init(
            api_key=settings.AGENTOPS_API_KEY,
            skip_auto_end_session=True,
            default_tags=["crewai"],
        )
        self._agentops_initialised = True

    def run(self, inputs: CrewInputs, output_dir: str | None = None) -> dict:
        """
        Run the full crew pipeline.

        Returns a dict with keys:
            raw         – raw CrewAI result object
            report_html – contents of the generated HTML report (str | None)
            output_dir  – directory where JSON artefacts were saved
        """
        self._init_agentops()

        if output_dir is None:
            output_dir = settings.OUTPUT_DIR

        crew = build_crew(output_dir=output_dir)
        raw = crew.kickoff(inputs=inputs.model_dump())

        report_path = os.path.join(output_dir, "step_4_procurement_report.html")
        report_html: str | None = None
        if os.path.exists(report_path):
            with open(report_path, "r", encoding="utf-8") as f:
                report_html = f.read()

        return {
            "raw": raw,
            "report_html": report_html,
            "output_dir": output_dir,
        }

    def load_json_artifact(self, filename: str, output_dir: str | None = None) -> dict | None:
        """Load a JSON step artefact from the output directory."""
        if output_dir is None:
            output_dir = settings.OUTPUT_DIR
        path = os.path.join(output_dir, filename)
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
