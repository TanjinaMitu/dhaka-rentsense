import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page Configuration
st.set_page_config(
    page_title="Dhaka RentSense", 
    page_icon="🏠", 
    layout="wide"
)

# Sidebar Information
st.sidebar.title("ℹ️ Project Info")
st.sidebar.info(
    "**Dhaka RentSense** predicts residential rental prices across Dhaka using an "
    "XGBoost Regressor trained on 28,000+ real estate listings."
)
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Model Metrics")
st.sidebar.metric(label="R² Accuracy Score", value="0.8640")
st.sidebar.metric(label="Mean Absolute Error (MAE)", value="৳3,029 BDT")

# Main Interface
st.title("🏠 Dhaka RentSense")
st.markdown("##### *Rental Market Intelligence & Price Prediction System*")
st.markdown("---")

@st.cache_resource
def load_model():
    return joblib.load("models/model.joblib")

try:
    model = load_model()
except Exception as e:
    st.error("Model artifact not found. Please run `python -m src.train` first.")
    st.stop()

col_input, col_display = st.columns([1, 1], gap="large")

with col_input:
    st.subheader("⚙️ Property Specifications")
    
    area = st.selectbox(
        "Location / Neighborhood", 
        ["Mirpur", "Mohammadpur", "Uttara", "Dhanmondi", "Gulshan", "Bashundhara R-A", "Banani", "Baridhara", "Badda", "Khilgaon"]
    )
    size_sqft = st.number_input("Apartment Size (sq ft)", min_value=200, max_value=6000, value=1200, step=50)
    
    c1, c2 = st.columns(2)
    with c1:
        bed = st.slider("Bedrooms", min_value=1, max_value=6, value=3)
    with c2:
        bath = st.slider("Bathrooms", min_value=1, max_value=6, value=3)

    predict_btn = st.button("🚀 Calculate Rent Estimate", use_container_width=True, type="primary")

with col_display:
    st.subheader("💡 Market Valuation Result")
    if predict_btn:
        input_df = pd.DataFrame([{
            'primary_area': area,
            'size_sqft': size_sqft,
            'Bed': bed,
            'Bath': bath
        }])
        
        pred_log = model.predict(input_df)[0]
        pred_bdt = np.expm1(pred_log)
        
        lower_bound = pred_bdt * 0.90
        upper_bound = pred_bdt * 1.10

        st.success(f"### Predicted Monthly Rent\n# ৳{pred_bdt:,.0f} BDT")
        
        m1, m2 = st.columns(2)
        m1.metric("Min Valuation (-10%)", f"৳{lower_bound:,.0f}")
        m2.metric("Max Valuation (+10%)", f"৳{upper_bound:,.0f}")
        
        st.caption("ℹ️ Estimates are calculated based on historic location-specific trends, square footage, and room counts.")
    else:
        st.info("👈 Adjust the property specifications on the left and click **Calculate Rent Estimate**.")