import joblib
import pandas as pd
import numpy as np

def test_model_artifact_exists():
    model = joblib.load("models/model.joblib")
    assert model is not None

def test_model_prediction_output():
    model = joblib.load("models/model.joblib")
    sample_data = pd.DataFrame([{
        'primary_area': 'Mirpur',
        'size_sqft': 1200,
        'Bed': 3,
        'Bath': 3
    }])
    
    pred_log = model.predict(sample_data)[0]
    pred_bdt = np.expm1(pred_log)
    
    assert 10000 <= pred_bdt <= 50000