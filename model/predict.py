from pathlib import Path
import joblib
import pandas as pd
import numpy as np
from schema.user_input import UserInput  # <-- Added missing import

# Get directory path of the current file (model folder)
MODEL_DIR = Path(__file__).resolve().parent

# Load model pipeline and saved columns
pipeline = joblib.load(MODEL_DIR / "house_price_pipeline.pkl")
saved_columns = joblib.load(MODEL_DIR / "model_columns.pkl")
MODEL_VERSION = "1.0"

def predict_house_price(data: UserInput):
    # Convert incoming JSON payload to DataFrame
    raw_df = pd.DataFrame([data.model_dump()])

    # Generate one-hot encoded columns for categorical features
    encoded_df = pd.get_dummies(raw_df, columns=["MSZoning", "Neighborhood"])

    # Align columns to match the exact 36 features expected by model
    aligned_df = encoded_df.reindex(columns=saved_columns, fill_value=0)

    # Pass through pipeline
    raw_prediction = pipeline.predict(aligned_df)[0]
    predicted_price = np.expm1(raw_prediction)
    
    return float(predicted_price)