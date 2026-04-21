import streamlit as st
import pandas as pd

def run():

    st.subheader("📂 Data Workspace")

    file = st.file_uploader("Upload Dataset", type=["csv"])

    if file is not None:
        try:
            df = pd.read_csv(file)

            st.session_state.datasets[file.name] = df
            st.session_state.current_df = df

            st.success(f"{file.name} uploaded successfully")

        except Exception as e:
            st.error(f"Error reading file: {e}")

    if st.session_state.datasets:

        st.write("### Available Datasets")

        selected = st.selectbox(
            "Select Dataset",
            list(st.session_state.datasets.keys())
        )

        if selected:
            st.session_state.current_df = st.session_state.datasets[selected]
            st.dataframe(st.session_state.current_df.head(50))