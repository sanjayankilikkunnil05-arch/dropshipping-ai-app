import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("final_model.pkl")

# Page config
st.set_page_config(page_title="Dropshipping AI", page_icon="🚀", layout="centered")

# Title
st.title("🚀 Dropshipping AI Analyzer")
st.subheader("Find Winning Products Using AI")

# Inputs
product_name = st.text_input("Product Name")

views = st.number_input("Views", min_value=0.0, value=0.0)
likes = st.number_input("Likes", min_value=0.0, value=0.0)
comments = st.number_input("Comments", min_value=0.0, value=0.0)

price = st.number_input("Price", min_value=0.0, value=0.0)
profit_margin = st.number_input("Profit Margin", min_value=0.0, value=0.0)

wow_factor = st.slider("Wow Factor", 1, 10, 1)
competition = st.slider("Competition", 1, 10, 1)

# Button
if st.button("🚀 Analyze Product"):

    try:
        # Derived features
        engagement_rate = (likes + comments) / views if views > 0 else 0
        profit_ratio = profit_margin / price if price > 0 else 0
        demand_score = views * engagement_rate

        # ⚠️ IMPORTANT: EXACT ORDER
        input_data = pd.DataFrame([[
            views,
            likes,
            comments,
            price,
            profit_margin,
            wow_factor,
            competition,
            engagement_rate,
            profit_ratio,
            demand_score
        ]], columns=[
            "views",
            "likes",
            "comments",
            "price",
            "profit_margin",
            "wow_factor",
            "competition",
            "engagement_rate",
            "profit_ratio",
            "demand_score"
        ])

        # Prediction
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.success("🔥 This product is WINNING!")
        else:
            st.error("❌ This product may NOT perform well.")

    except Exception as e:
        st.error(f"Error: {e}")
