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
