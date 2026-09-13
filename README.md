# 🏠 Dhaka RentSense: Rental Price Prediction Pipeline

An end-to-end Machine Learning system and interactive web application that predicts residential rental prices in Dhaka, Bangladesh, using modular Python pipelines, MySQL, XGBoost, and Streamlit.

---

## 📌 Features
- **Automated Data Ingestion:** Loads raw listing data into MySQL using SQLAlchemy.
- **Data Cleaning & Feature Engineering:** Extracts numerical attributes from complex string formats.
- **Machine Learning Pipeline:** Trains an **XGBoost Regressor** with One-Hot Encoding and log-transformed targets.
- **Unit Testing:** Automated testing using `pytest` covering preprocessing logic and artifact verification.
- **Interactive Dashboard:** Streamlit interface for live market valuation and confidence intervals.

---

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Data Manipulation & ML:** Pandas, NumPy, Scikit-Learn, XGBoost
- **Database:** MySQL, SQLAlchemy
- **Model Serialization:** Joblib
- **Testing:** Pytest
- **Frontend App:** Streamlit

---

## 📈 Model Performance
- **R² Score:** `0.8640`
- **Mean Absolute Error (MAE):** `~৳3,029.05 BDT`

---

## 🚀 Getting Started

### 1. Setup Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\Activate.ps1