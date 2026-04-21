import streamlit as st

def run():

    st.subheader("⬇️ Export Data")

    df = st.session_state.current_df

    if df is None:
        st.warning("Upload dataset first")
        return

    try:
        csv = df.to_csv(index=False).encode()

        st.download_button(
            "Download CSV",
            csv,
            "cleaned_data.csv"
        )

    except Exception as e:
        st.error(f"Export error: {e}")