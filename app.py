import os
import streamlit as st

from config import settings
from controllers import CrewController
from views import render_sidebar, render_results

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Procurement AI Agent",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🛒 Procurement AI Agent")
st.markdown(
    "Powered by **CrewAI** · GPT-4o · Tavily Search · ScrapeGraph\n\n"
    "Fill in the form on the left and click **Run Agent** to start the pipeline."
)

# ── API key validation ────────────────────────────────────────────────────────
missing_keys = settings.validate()
if missing_keys:
    st.error(
        f"Missing environment variables: **{', '.join(missing_keys)}**\n\n"
        "Please create a `.env` file based on `.env.example` and restart the app."
    )
    st.stop()

# ── View: sidebar inputs ──────────────────────────────────────────────────────
crew_inputs = render_sidebar()

# ── Controller: run the crew ──────────────────────────────────────────────────
if crew_inputs is not None:
    controller = CrewController()

    with st.spinner("Running the AI agent pipeline... this may take a few minutes."):
        try:
            result = controller.run(crew_inputs)
        except Exception as exc:
            st.error(f"An error occurred during the agent run:\n\n```\n{exc}\n```")
            st.stop()

    # ── View: results ─────────────────────────────────────────────────────────
    render_results(result, controller)
else:
    st.info("Configure your search in the sidebar and click **Run Agent**.")
