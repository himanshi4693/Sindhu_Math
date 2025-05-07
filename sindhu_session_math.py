import streamlit as st
from pathlib import Path
import base64

# ✅ MUST be first Streamlit command
st.set_page_config(page_title="💆🏽‍♀️ Sindhu's Therapy Fee Calculator", page_icon="💰")

# Function to set background image
def set_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background
set_bg_from_local("blue_wallpaper.png")

# 🎨 Change text color to dark blue
st.markdown("""
    <style>
    html, body, [class*="st-"] {
        color: #196A8A;
    }
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title and UI
st.title("🧠💸 Sindhu's Therapy Session Payment Calculator 💬✨")

# Inputs
base_charge = st.number_input("💵 Enter base charge for 60 minutes:", min_value=0, step=1)
minutes = st.number_input("⏱️ Enter session duration (in minutes):", min_value=0, step=1)

if base_charge and minutes:
    charge_per_min = base_charge / 60
    additional_mins = minutes - 60

    if additional_mins <= 6:
        payment = base_charge
    else:
        extra_charge = additional_mins * charge_per_min
        payment = base_charge + extra_charge

    payment = payment

    st.success(f"💰 Payment due: ₹{payment}")