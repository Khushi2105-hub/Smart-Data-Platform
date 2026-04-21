import streamlit as st

def run():

    st.subheader("📊 Dashboard")

    df = st.session_state.current_df

    if df is None:
        st.info("Upload dataset in Workspace first")
        return

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing", df.isnull().sum().sum())
    col4.metric("Duplicates", df.duplicated().sum())

    st.dataframe(df.head(50))