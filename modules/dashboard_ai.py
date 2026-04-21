import streamlit as st
import pandas as pd
import plotly.express as px

def run():

    st.subheader("⚡ AI Dashboard Generator")

    df = st.session_state.current_df

    if df is None:
        st.warning("Upload dataset first")
        return

    if st.button("🚀 Generate Smart Dashboard"):

        st.success("AI is generating dashboard...")

        # ================= BASIC STATS =================
        st.markdown("### 📊 Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", df.isnull().sum().sum())

        # ================= NUMERIC CHART =================
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

        if len(numeric_cols) > 0:
            st.markdown("### 📈 Numeric Analysis")

            col = numeric_cols[0]

            fig = px.histogram(df, x=col, title=f"{col} Distribution")
            st.plotly_chart(fig, use_container_width=True)

        # ================= CATEGORICAL CHART =================
        cat_cols = df.select_dtypes(include=['object']).columns

        if len(cat_cols) > 0:
            st.markdown("### 📊 Category Analysis")

            col = cat_cols[0]

            counts = df[col].value_counts().reset_index()
            counts.columns = [col, "Count"]

            fig = px.bar(counts, x=col, y="Count", title=f"{col} Distribution")
            st.plotly_chart(fig, use_container_width=True)

        # ================= CORRELATION =================
        if len(numeric_cols) > 1:
            st.markdown("### 🔥 Correlation Heatmap")

            corr = df[numeric_cols].corr()

            fig = px.imshow(corr, text_auto=True, title="Correlation Matrix")
            st.plotly_chart(fig, use_container_width=True)

        # ================= QUICK INSIGHT =================
        st.markdown("### 🧠 AI Insights")

        if len(numeric_cols) > 0:
            st.info(f"Dataset has {len(numeric_cols)} numeric columns for analysis")

        if len(cat_cols) > 0:
            st.info(f"Dataset has {len(cat_cols)} categorical columns")

        if df.isnull().sum().sum() > 0:
            st.warning("Dataset contains missing values")