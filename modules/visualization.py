import streamlit as st
import pandas as pd
import plotly.express as px

def run():

    st.subheader("📊 Smart Visualization")

    df = st.session_state.current_df

    if df is None:
        st.warning("Upload dataset first")
        return

    # ================= COLUMN SELECT =================
    column = st.selectbox("Select Column", df.columns)

    col_type = df[column].dtype

    st.markdown("### 🧠 AI Recommendation")

    # ================= AI LOGIC =================
    if pd.api.types.is_numeric_dtype(df[column]):

        st.success("Recommended: Histogram")

        fig = px.histogram(df, x=column, title=f"{column} Distribution")
        st.plotly_chart(fig, use_container_width=True)

        # Optional override
        if st.checkbox("Try Line Chart"):
            fig2 = px.line(df, y=column, title=f"{column} Trend")
            st.plotly_chart(fig2, use_container_width=True)

    else:
        st.success("Recommended: Bar Chart")

        counts = df[column].value_counts().reset_index()
        counts.columns = [column, "Count"]

        fig = px.bar(counts, x=column, y="Count", title=f"{column} Distribution")
        st.plotly_chart(fig, use_container_width=True)

        # Optional override
        if st.checkbox("Try Pie Chart"):
            fig2 = px.pie(counts, names=column, values="Count", title=f"{column} Breakdown")
            st.plotly_chart(fig2, use_container_width=True)

    # ================= EXTRA SMART FEATURE =================
    st.markdown("### ⚡ Quick Insight")

    if pd.api.types.is_numeric_dtype(df[column]):
        st.info(f"Mean: {df[column].mean():.2f} | Max: {df[column].max()} | Min: {df[column].min()}")
    else:
        top = df[column].value_counts().idxmax()
        st.info(f"Most frequent value: {top}")