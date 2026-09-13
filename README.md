# 🏠 Dhaka RentSense | Residential Rental Valuation Engine

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-111111?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Passed-0A9EDC?style=flat&logo=pytest&logoColor=white)

An end-to-end Machine Learning system and production-ready web application designed to estimate residential rental prices across Dhaka, Bangladesh. Built with modular Python software design, automated MySQL data ingestion, XGBoost modeling, unit tests, and an interactive Streamlit dashboard.

---

## 💾 Data & Pipeline Overview

The underlying dataset contains **28,800+ real estate property listings** across Dhaka.

- **Data Source:** Web-scraped property listings derived from [Bproperty.com](https://www.bproperty.com) (available via Kaggle).
- **Source File:** `data/raw/houserentdhaka.csv`
- **Database Storage:** Automated loading into a **MySQL** relational database table (`raw_rentals`) using SQLAlchemy ORM and PyMySQL.
- **Data Engineering Steps:** 
  1. Ingest raw tabular data into MySQL via automated Python scripts.
  2. Query records dynamically from the database for training runs.
  3. Preprocess raw text fields (e.g., parsing string formats like `"20 Thousand"` or `"1.5 Lakh"` into BDT floats and cleaning square footage values).

---

## 📐 System Architecture

```text
┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│  Raw Data                 │ ───> │  MySQL Database           │ ───> │  Feature Engineering      │
│  (houserentdhaka.csv)     │      │  (raw_rentals table)      │      │  & Preprocessing          │
└───────────────────────────┘      └───────────────────────────┘      └─────────────┬─────────────┘
                                                                                    │
┌───────────────────────────┐      ┌───────────────────────────┐                    │
│  Streamlit Dashboard      │ <─── │  Serialized Model         │ <──────────────────┘
│  (Interactive Valuation)  │      │  (model.joblib)           │
└───────────────────────────┘      └───────────────────────────┘

## 📌 Key Features

- **Automated MySQL Ingestion:** Loads `houserentdhaka.csv` directly into MySQL via `src/data_ingestion.py`.

- **Robust Feature Engineering:** Cleans string-formatted rents and standardizes locations, square footage, bedrooms, and bathrooms.

- **High-Performance Modeling:** Trains an XGBoost Regressor on log-transformed targets to handle positive price skew.

- **Automated Testing Suite:** Integrated `pytest` suite covering data-cleaning logic and model inference verification.

- **Interactive UI:** Dual-column Streamlit interface displaying real-time predictions with **±10% market confidence bounds**.

## Repository Structure

dhaka-rentsense/
├── app/
│   └── app.py                # Streamlit user interface
├── data/
│   └── raw/
│       └── houserentdhaka.csv# Raw Bproperty listing dataset (28,800+ rows)
├── models/
│   └── model.joblib          # Serialized XGBoost artifact
├── src/
│   ├── data_ingestion.py     # MySQL database loader
│   ├── data_cleaning.py      # Preprocessing & string parsing
│   ├── feature_engineering.py# Feature transformations
│   ├── predict.py            # Model inference runner
│   └── train.py              # Model training script
├── tests/
│   ├── test_cleaning.py      # Preprocessing unit tests
│   └── test_predict.py       # Inference unit tests
├── .gitignore
├── pytest.ini                # Pytest path configuration
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies

## 🛠️ Tech Stack

- **Core Language:** Python 3.13
- **Database:** MySQL, SQLAlchemy, PyMySQL
- **Data Engineering & ML:** Pandas, NumPy, Scikit-Learn, XGBoost, Joblib
- **Testing:** Pytest
- **Frontend App:** Streamlit

## 📈 Model Performance

| **Metric**      | **Score**             | **Description**                                           |
| --------------- | --------------------- | --------------------------------------------------------- |
| **$R^2$ Score** | **`0.8640`**           | Explains **86.4%** of rental price variance across Dhaka. |
| **MAE**         | **`~৳3,029.05 BDT`**   | Average absolute prediction error on out-of-sample properties. |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/dhaka-rentsense.git
cd dhaka-rentsense
```

### 2. Set Up Environment & Install Dependencies

```bash
python -m venv venv

# Windows PowerShell
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 3. Run the Pipeline

```bash
# Ingest CSV dataset into MySQL
python -m src.data_ingestion

# Train XGBoost model
python -m src.train

# Run automated tests
pytest
```

### 4. Launch the Web Application

```bash
streamlit run app/app.py
```

**That's it!** The pipeline will ingest the dataset, train the model, run tests, and launch the Streamlit prediction app.
