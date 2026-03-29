import streamlit as st
import pandas as pd
import os
from groq import Groq
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="PragyanAI Advanced Dashboard", layout="wide")

st.title(" PragyanAI Advanced Streamlit UI Dashboard")

# -----------------------------
# LOAD DATA (SAFE)
# -----------------------------
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

file_path = "student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv"

if os.path.exists(file_path):
    df = load_data(file_path)
else:
    st.error("❌ Dataset not found")
    st.stop()
# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
st.sidebar.title(" Navigation Project Menu")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Dashboard", "Form", "Session State", "All Inputs","Advanced Media"]
)

# =============================
# 🏠 HOME
# =============================
if page == "Home":
    st.subheader("Welcome to PragyanAI Dashboard")
    st.write("This app demonstrates all major Streamlit UI features")
    st.image("PragyanAI_Transperent.png")
    # -----------------------------
    # SAFE DATA LOADING
    # -----------------------------
    uploaded_file = st.file_uploader("Upload CSV (Recommended)", type=["csv"])
    @st.cache_data
    def load_data(path):
        return pd.read_csv(path)
    if uploaded_file:
        df = pd.read_csv(uploaded_file)    
    st.success("✅ Data Loaded Successfully")
# =============================
# 📊 DASHBOARD (TABS)
# =============================
elif page == "Dashboard":

    st.subheader(" Data Analytics Dashboard")

    tab1, tab2, tab3 = st.tabs([" Data", " Charts", " KPIs"])

    # -------------------------
    # TAB 1: DATA
    # -------------------------
    with tab1:
        st.write("### Dataset Preview")
        st.dataframe(df.head())
        st.write("### Dataset's Basic Descriptive Statistic  ### ")
        st.write(df.decribe())
    # -------------------------
    # TAB 2: CHARTS
    # -------------------------
    with tab2:
        st.write("### Revenue Trend")
        st.line_chart(df["Revenue"])

        st.write("### Revenue by Program")
        st.bar_chart(df.groupby("Program_Type")["Revenue"].sum())

    # -------------------------
    # TAB 3: KPIs
    # -------------------------
    with tab3:
        col1, col2, col3 = st.columns(3)

        total_students = len(df)
        avg_price = df["Final_Price"].mean()
        conversion_rate = df["Converted"].mean() * 100

        col1.metric("Total Students", total_students)
        col2.metric("Avg Price", f"₹{avg_price:,.0f}")
        col3.metric("Conversion Rate", f"{conversion_rate:.2f}%")
