import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score

from src.db_connection import get_mysql_engine
from src.data_cleaning import parse_price, parse_sqft, extract_primary_area

def run_training_pipeline():
    engine = get_mysql_engine()
    query = "SELECT Location, Area, Bed, Bath, Price FROM raw_rentals"
    
    print("Fetching raw rental data from MySQL database...")
    df = pd.read_sql(query, con=engine)
    print(f"Retrieved {len(df)} records from MySQL.")

    # Apply data transformations
    print("Cleaning data and extracting features...")
    df['rent_bdt'] = df['Price'].apply(parse_price)
    df['size_sqft'] = df['Area'].apply(parse_sqft)
    df['primary_area'] = df['Location'].apply(extract_primary_area)
    
    # Filter valid rows and outliers
    df = df.dropna(subset=['rent_bdt', 'size_sqft']).copy()
    df = df[(df['size_sqft'] >= 200) & (df['size_sqft'] <= 6000)]
    df = df[(df['rent_bdt'] >= 5000) & (df['rent_bdt'] <= 500000)]

    X = df[['primary_area', 'size_sqft', 'Bed', 'Bath']]
    y = np.log1p(df['rent_bdt'])  # Stabilize price distribution using log-transform

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['primary_area']),
            ('num', 'passthrough', ['size_sqft', 'Bed', 'Bath'])
        ]
    )

    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', XGBRegressor(n_estimators=150, learning_rate=0.08, random_state=42))
    ])

    print("Training XGBoost regression model...")
    model_pipeline.fit(X_train, y_train)

    # Convert log predictions back to original BDT scale
    y_pred_log = model_pipeline.predict(X_test)
    y_pred = np.expm1(y_pred_log)
    y_true = np.expm1(y_test)

    print("\n--- Training Evaluation Metrics ---")
    print(f"MAE: ৳{mean_absolute_error(y_true, y_pred):,.2f} BDT")
    print(f"R² Score: {r2_score(y_true, y_pred):.4f}")

    # Save model artifact
    joblib.dump(model_pipeline, "models/model.joblib")
    print("\nModel saved successfully to 'models/model.joblib'!")

if __name__ == "__main__":
    run_training_pipeline()