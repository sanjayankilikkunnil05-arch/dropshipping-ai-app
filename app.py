import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="Dropshipping AI", page_icon="🚀", layout="centered")

# Custom CSS (STARTUP LOOK)
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
h1 {
    text-align: center;
    color: #00ffcc;
}
.stButton>button {
    background-color: #00ffcc;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("final_model.pkl")

features = [
    'views', 'likes', 'comments', 'price',
    'profit_margin', 'wow_factor', 'competition',
    'engagement_rate', 'demand_score', 'profit_ratio'
]

def calculate_score(row):
    row = row.copy()

    row['engagement_rate'] = row['likes'] / (row['views'] + 1)
    row['demand_score'] = row['views'] + row['comments']
    row['profit_ratio'] = row['profit_margin'] / (row['price'] + 1)

    input_data = pd.DataFrame([row])[features]
    prob = model.predict_proba(input_data)
    return prob[0][1] * 100

# UI Header
st.title("🚀 Dropshipping AI Analyzer")
st.markdown("### Find Winning Products Using AI")

# Inputs
name = st.text_input("Product Name")

col1, col2 = st.columns(2)

with col1:
    views = st.number_input("Views", min_value=0.0)
    likes = st.number_input("Likes", min_value=0.0)
    comments = st.number_input("Comments", min_value=0.0)

with col2:
    price = st.number_input("Price", min_value=0.0)
    profit = st.number_input("Profit Margin", min_value=0.0)
    wow = st.slider("Wow Factor", 1, 5)
    comp = st.slider("Competition", 1, 5)

# Button
if st.button("🚀 Analyze Product"):

    if likes > views:
        st.error("❌ Likes cannot be greater than Views")
    else:
        row = {
            "views": views,
            "likes": likes,
            "comments": comments,
            "price": price,
            "profit_margin": profit,
            "wow_factor": wow,
            "competition": comp
        }

        score = calculate_score(row)

        st.markdown(f"## 🔥 Score: {score:.2f}/100")

        if score > 80:
            st.success("🔥 WINNING PRODUCT!")
        elif score > 60:
            st.info("✅ GOOD PRODUCT")
        else:
            st.warning("⚠️ RISKY PRODUCT")