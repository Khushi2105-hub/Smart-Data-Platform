import streamlit as st

def run():

    df = st.session_state.current_df

    st.subheader("🧹 Data Studio")

    if df is None:
        st.warning("Upload dataset first")
        return

    option = st.selectbox("Missing Values", ["None", "Drop Rows", "Fill Mean"])
    dup = st.checkbox("Remove Duplicates")

    # 🔥 ADD THIS STATE
    if "cleaned_flag" not in st.session_state:
        st.session_state.cleaned_flag = False

    if st.button("Apply Cleaning"):

        temp = df.copy()

        if option == "Drop Rows":
            temp = temp.dropna()

        elif option == "Fill Mean":
            temp = temp.fillna(temp.mean(numeric_only=True))

        if dup:
            temp = temp.drop_duplicates()

        st.session_state.current_df = temp
        st.session_state.cleaned_flag = True  # ✅ important

    # ✅ SHOW SUCCESS ONLY WHEN CLEANED
    if st.session_state.cleaned_flag:
        st.success("✨ Cleaning completed successfully")

    st.dataframe(st.session_state.current_df)