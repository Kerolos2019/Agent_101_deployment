import streamlit as st
from models.schemas import CrewInputs


def render_sidebar() -> CrewInputs | None:
    """Render the sidebar input form and return CrewInputs when submitted."""
    st.sidebar.title("Procurement Agent")
    st.sidebar.markdown("Configure your search and click **Run**.")

    with st.sidebar.form("crew_inputs"):
        product_name = st.text_input(
            "Product to search for",
            value="coffee machine for the office",
        )

        websites_raw = st.text_area(
            "Target websites (one per line)",
            value="www.amazon.eg\nwww.jumia.com.eg\nwww.noon.com/egypt-en",
        )

        country_name = st.text_input("Country", value="Egypt")

        language = st.selectbox(
            "Search language",
            options=["English", "Arabic", "French", "German", "Spanish"],
            index=0,
        )

        col1, col2 = st.columns(2)
        with col1:
            no_keywords = st.number_input(
                "Max keywords", min_value=1, max_value=20, value=10
            )
        with col2:
            top_recommendations_no = st.number_input(
                "Top results", min_value=1, max_value=30, value=10
            )

        score_th = st.slider(
            "Min relevance score", min_value=0.0, max_value=1.0, value=0.10, step=0.05
        )

        submitted = st.form_submit_button("Run Agent", use_container_width=True)

    if not submitted:
        return None

    websites_list = [w.strip() for w in websites_raw.splitlines() if w.strip()]

    return CrewInputs(
        product_name=product_name,
        websites_list=websites_list,
        country_name=country_name,
        no_keywords=int(no_keywords),
        language=language,
        score_th=score_th,
        top_recommendations_no=int(top_recommendations_no),
    )
