import os
import json
import streamlit as st
from controllers import CrewController


def render_results(result: dict, controller: CrewController) -> None:
    """Display the crew results: step artefacts + HTML report."""

    st.success("Agent run completed!")

    output_dir = result["output_dir"]

    # ── Step artefacts ────────────────────────────────────────────────────────
    with st.expander("Step 1 — Suggested Search Queries", expanded=False):
        data = controller.load_json_artifact(
            "step_1_suggested_search_queries.json", output_dir
        )
        if data:
            for i, q in enumerate(data.get("queries", []), 1):
                st.write(f"{i}. {q}")
        else:
            st.info("No output found.")

    with st.expander("Step 2 — Search Results", expanded=False):
        data = controller.load_json_artifact("step_2_search_results.json", output_dir)
        if data:
            results = data.get("results", [])
            st.write(f"**{len(results)} results found**")
            for r in results:
                st.markdown(
                    f"- [{r.get('title', 'No title')}]({r.get('url', '#')}) "
                    f"(score: {r.get('score', 0):.2f})"
                )
        else:
            st.info("No output found.")

    with st.expander("Step 3 — Scraped Products", expanded=False):
        data = controller.load_json_artifact("step_3_scraped_products.json", output_dir)
        if data:
            products = data.get("products", [])
            st.write(f"**{len(products)} products extracted**")
            for p in products:
                title = p.get("product_title", "Unknown")
                price = p.get("product_current_price", "N/A")
                url = p.get("product_url", "#")
                rank = p.get("agent_recommendation_rank", "N/A")
                st.markdown(f"- **{title}** — {price} | Rank: {rank}/5 | [Link]({url})")
        else:
            st.info("No output found.")

    # ── HTML Report ───────────────────────────────────────────────────────────
    st.subheader("Procurement Report")
    report_html = result.get("report_html")
    if report_html:
        report_path = os.path.join(output_dir, "step_4_procurement_report.html")
        st.download_button(
            label="Download HTML Report",
            data=report_html,
            file_name="procurement_report.html",
            mime="text/html",
            use_container_width=True,
        )
        st.components.v1.html(report_html, height=800, scrolling=True)
    else:
        st.warning("HTML report was not generated.")
