from fastapi import FastAPI
from schema.user_input import UserInput
from model.predict import predict_house_price

app = FastAPI(title="House Price Prediction API")

@app.get("/")
def health():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: UserInput):
    predicted_price = predict_house_price(data)
    return {"predicted_price": round(predicted_price, 2)}