import streamlit as st
import pandas as pd
import joblib
import time

# Load model
model = joblib.load("final_model.pkl")

# Page config
st.set_page_config(page_title="Dropshipping AI", page_icon="🚀", layout="centered")

# ---------- UI DESIGN ----------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
h1 {
    text-align: center;
}
.stButton>button {
    background-color: #00c896;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🚀 Dropshipping AI Analyzer")
st.markdown("### 📊 AI-powered product success prediction for dropshipping")

# ---------- INPUTS ----------
product_name = st.text_input("Product Name")

col1, col2 = st.columns(2)

with col1:
    views = st.number_input("Views", min_value=0.0, step=100.0)
    likes = st.number_input("Likes", min_value=0.0, step=100.0)
    comments = st.number_input("Comments", min_value=0.0, step=100.0)

with col2:
    price = st.number_input("Price", min_value=0.0, step=10.0)
    profit_margin = st.number_input("Profit Margin", min_value=0.0, step=10.0)
    wow_factor = st.slider("Wow Factor", 1, 10, 5)
    competition = st.slider("Competition", 1, 10, 5)

# ---------- BUTTON ----------
if st.button("🚀 Analyze Product"):

    # Validation
    if views == 0 or likes == 0:
        st.warning("⚠️ Please enter valid data (views & likes should not be 0)")
    else:
        # Loading animation
        with st.spinner("Analyzing product with AI..."):
            time.sleep(2)

            # Create dataframe
            input_data = pd.DataFrame({
                'views': [views],
                'likes': [likes],
                'comments': [comments],
                'price': [price],
                'profit_margin': [profit_margin],
                'wow_factor': [wow_factor],
                'competition': [competition]
            })

            # Prediction
            prediction = model.predict(input_data)[0]

            # Show score
            st.success(f"🔥 AI Score: {prediction}/100")

            # Result message
            if prediction > 80:
                st.markdown("🚀 **High Potential Product!**")
            elif prediction > 50:
                st.markdown("⚡ **Moderate Potential**")
            else:
                st.markdown("❌ **Low Potential**")
