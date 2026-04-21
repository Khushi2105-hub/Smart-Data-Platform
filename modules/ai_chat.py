import streamlit as st
import pandas as pd

def run():

    st.subheader("💬 Chat with Your Data")

    df = st.session_state.current_df

    if df is None:
        st.warning("Upload dataset first")
        return

    query = st.text_input("Ask something about your data")

    if query:

        query = query.lower()

        # ================= BASIC LOGIC =================

        # MEAN / AVERAGE
        if "average" in query or "mean" in query:
            for col in df.select_dtypes(include=['int64', 'float64']).columns:
                if col.lower() in query:
                    st.success(f"Average of {col}: {df[col].mean():.2f}")
                    return

        # MAX
        if "max" in query or "highest" in query:
            for col in df.select_dtypes(include=['int64', 'float64']).columns:
                if col.lower() in query:
                    st.success(f"Max of {col}: {df[col].max()}")
                    return

        # MIN
        if "min" in query or "lowest" in query:
            for col in df.select_dtypes(include=['int64', 'float64']).columns:
                if col.lower() in query:
                    st.success(f"Min of {col}: {df[col].min()}")
                    return

        # COUNT
        if "count" in query:
            st.success(f"Total rows: {df.shape[0]}")
            return

        # VALUE COUNTS
        if "top" in query or "most" in query:
            for col in df.select_dtypes(include=['object']).columns:
                if col.lower() in query:
                    top = df[col].value_counts().idxmax()
                    st.success(f"Most common in {col}: {top}")
                    return

        # SHOW DATA
        if "show" in query:
            st.dataframe(df.head())
            return

        # FALLBACK
        st.warning("Try asking about average, max, count, or top values.")