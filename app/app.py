import joblib
from fastapi import FastAPI, HTTPException
import numpy as np
import pandas as pd
from pydantic import BaseModel
from model.predict import MODEL_VERSION, model, predict_output
from schema.user_input import UserInput

app = FastAPI(title="House Price Prediction API")


@app.get("/")
def home():
    return {"message": "house price predictor api"}


@app.get("/health")
def health():
    return {"status": "ok", "version": MODEL_VERSION}


@app.post("/predict")
def predict_houseprice(data: UserInput):
    if model is None:
        raise HTTPException(
            status_code=500, detail="Model file failed to load."
        )

    payload = data.model_dump()

    # Derived bathroom calculations
    full_bath = int(payload["total_bath"])
    half_bath = 1 if (payload["total_bath"] % 1) >= 0.5 else 0

    # Build exact dictionary matching ALL pipeline expectations
    user_input_dict = {
        # 1. UI direct features & engineered features
        "house_age": payload["house_age"],
        "total_sqft": payload["total_sqft"],
        "area_per_room": (
            payload["total_sqft"] / 6.0 if payload["total_sqft"] > 0 else 0.0
        ),
        "overall_space": payload["total_sqft"],
        "garage_area_ratio": (
            payload["GarageArea"] / payload["total_sqft"]
            if payload["total_sqft"] > 0
            else 0.0
        ),
        "GarageCars": payload["GarageCars"],
        "GarageArea": payload["GarageArea"],
        "OverallQual": payload["OverallQual"],
        "OverallCond": payload["OverallCond"],
        "Fireplaces": payload["Fireplaces"],
        "KitchenQual": payload["KitchenQual"],
        "ExterQual": payload["ExterQual"],
        "Neighborhood": payload["Neighborhood"],
        "YearBuilt": 2026 - payload["house_age"],
        "GrLivArea": payload["total_sqft"],
        "FullBath": full_bath,
        "HalfBath": half_bath,
        "BedroomAbvGr": 3,
        "TotalBsmtSF": 0.0,
        "LotArea": 8500.0,
    }

    try:
        input_df = pd.DataFrame([user_input_dict])
        prediction = predict_output(input_df)

        return {"predicted_price": round(float(prediction), 2)}

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Prediction error: {str(e)}"
        )
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)