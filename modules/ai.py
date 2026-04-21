import streamlit as st
import pandas as pd

def run():

    st.subheader("✨ AI Insights")

    df = st.session_state.current_df

    if df is None:
        st.warning("Please upload dataset first")
        return

    # ================= BASIC INFO =================
    st.markdown("### 📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    # ================= DATA TYPES =================
    st.markdown("### 🧠 Column Intelligence")

    col_types = pd.DataFrame({
        "Column": df.columns,
        "Type": df.dtypes.astype(str)
    })

    st.dataframe(col_types)

    # ================= MISSING VALUES =================
    st.markdown("### ⚠️ Missing Values Analysis")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        st.success("No missing values found 🎉")
    else:
        st.dataframe(missing)

    # ================= DUPLICATES =================
    st.markdown("### 🔁 Duplicate Detection")

    duplicates = df.duplicated().sum()

    if duplicates == 0:
        st.success("No duplicate records found 🎉")
    else:
        st.warning(f"{duplicates} duplicate rows detected")

    # ================= SMART SUGGESTIONS =================
    st.markdown("### 💡 Smart Suggestions")

    suggestions = []

    if df.isnull().sum().sum() > 0:
        suggestions.append("• Handle missing values (Mean / Drop)")

    if duplicates > 0:
        suggestions.append("• Remove duplicate records")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) > 0:
        suggestions.append("• Normalize numeric columns")

    cat_cols = df.select_dtypes(include=['object']).columns

    if len(cat_cols) > 0:
        suggestions.append("• Encode categorical variables")

    if suggestions:
        for s in suggestions:
            st.markdown(s)
    else:
        st.success("Your dataset looks clean and ready 🚀")

    # ================= AUTO INSIGHT =================
    st.markdown("### 🔍 Quick Insight")

    if len(numeric_cols) > 0:
        st.info(f"Dataset contains {len(numeric_cols)} numeric columns suitable for analysis")

    if len(cat_cols) > 0:
        st.info(f"Dataset contains {len(cat_cols)} categorical columns")