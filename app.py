import streamlit as st
import time

st.set_page_config(page_title="Smart Data Platform", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

/* ===== GLOBAL ===== */
.stApp {
    background: #0f0f1a;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: #141427;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ===== HERO ===== */
.hero {
    padding: 20px;
    border-radius: 12px;
    background: #1a1a2e;
    margin-bottom: 20px;
}

/* ===== TOOLTIP CARD ===== */
.tooltip-card {
    position: relative;
    padding: 16px;
    border-radius: 12px;
    background: #1e1e2f;
    border: 1px solid rgba(255,255,255,0.06);
    text-align: center;
    transition: 0.25s;
    cursor: pointer;
}

.tooltip-card:hover {
    transform: translateY(-4px);
    border: 1px solid #7b2ff7;
    box-shadow: 0px 8px 25px rgba(123,47,247,0.35);
}

/* ===== TOOLTIP TEXT ===== */
.tooltip-text {
    visibility: hidden;
    opacity: 0;
    width: 220px;
    background-color: #2a2a3f;
    color: #fff;
    text-align: center;
    padding: 8px;
    border-radius: 8px;
    position: absolute;
    z-index: 1;
    bottom: 120%;
    left: 50%;
    transform: translateX(-50%);
    transition: 0.3s;
    font-size: 12px;
}

.tooltip-card:hover .tooltip-text {
    visibility: visible;
    opacity: 1;
}

/* ===== BUTTON ===== */
button {
    border-radius: 8px !important;
    background: linear-gradient(135deg, #7b2ff7, #ff00cc) !important;
    color: white !important;
}

/* ===== LOADER ===== */
.loader-container {
    margin-top: 10px;
    margin-bottom: 10px;
}

.loader-bar {
    height: 4px;
    width: 0%;
    background: linear-gradient(90deg, #7b2ff7, #ff00cc);
    border-radius: 10px;
    animation: loadAnim 1s ease forwards;
}

@keyframes loadAnim {
    from { width: 0%; }
    to { width: 100%; }
}

/* ===== RESET POPUP ===== */
.popup-center {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #1e1e2f;
    padding: 20px 30px;
    border-radius: 12px;
    border: 1px solid #7b2ff7;
    box-shadow: 0px 10px 40px rgba(123,47,247,0.5);
    text-align: center;
    z-index: 9999;
}

</style>
""", unsafe_allow_html=True)

# ================= SESSION =================
if "datasets" not in st.session_state:
    st.session_state.datasets = {}

if "current_df" not in st.session_state:
    st.session_state.current_df = None

# ================= HERO =================
st.markdown("""
<div class="hero">
    <h3>💜 Smart Data Cleaning and Data Visualising 💜</h3>
    <p style="color:#aaa;">Insights • Cleaning • Visualization • AI Assist</p>
</div>
""", unsafe_allow_html=True)

# ================= FEATURES (HOVER TOOLTIP) =================
col1, col2, col3, col4 = st.columns(4)

col1.markdown("""
<div class="tooltip-card">
<b>📂 Multi Dataset</b>
<div class="tooltip-text">
Upload and switch between multiple datasets easily
</div>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class="tooltip-card">
<b>🧹 Smart Cleaning</b>
<div class="tooltip-text">
Automatically handle missing values and remove duplicates
</div>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class="tooltip-card">
<b>📊 Auto Visualization</b>
<div class="tooltip-text">
Generate charts based on your data type automatically
</div>
</div>
""", unsafe_allow_html=True)

col4.markdown("""
<div class="tooltip-card">
<b>✨ AI Insights</b>
<div class="tooltip-text">
Get quick insights and summaries from your dataset
</div>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Workspace", "Data Studio", "Analytics", "AI Insights", "AI Dashboard", "Export"]
)

# ================= RESET PLATFORM =================
st.sidebar.markdown("---")

if st.sidebar.button("🔄 Reset Platform"):
    popup = st.empty()

    popup.markdown("""
    <div class="popup-center">
        💜 Resetting platform...
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.5)

    st.session_state.datasets = {}
    st.session_state.current_df = None

    if "cleaned_flag" in st.session_state:
        st.session_state.cleaned_flag = False

    popup.empty()
    st.rerun()

# ================= LOADER FUNCTION =================
def show_loader(message):
    placeholder = st.empty()

    placeholder.markdown("""
    <div class="loader-container">
        <div class="loader-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    st.caption(message)

    time.sleep(1)

    placeholder.empty()

# ================= IMPORT MODULES =================
import modules.dashboard as dashboard
import modules.dashboard_ai as dashboard_ai
import modules.workspace as workspace
import modules.cleaning as cleaning
import modules.visualization as visualization
import modules.ai as ai
import modules.ai_chat as ai_chat
import modules.export as export

# ================= ROUTING =================
if menu == "Dashboard":
    dashboard.run()

elif menu == "AI Dashboard":
    show_loader("Generating AI dashboard...")
    dashboard_ai.run()
    
elif menu == "Workspace":
    show_loader("Uploading dataset...")
    workspace.run()

elif menu == "Data Studio":
    show_loader("Applying cleaning...")
    cleaning.run()

elif menu == "Analytics":
    show_loader("Generating visualization...")
    visualization.run()

elif menu == "AI Insights":
    show_loader("Analyzing dataset...")
    ai.run()
    st.markdown("---")
    ai_chat.run()

elif menu == "Export":
    show_loader("Preparing download...")
    export.run()