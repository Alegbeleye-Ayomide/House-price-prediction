import joblib
import pandas as pd
# Load model pipeline

model = joblib.load("model/house_price_pipeline.pkl")
joblib.dump(model, "model/house_price_pipeline.pkl", protocol=4)

MODEL_VERSION = 1.0
def predict_output(user_input: dict):

    input_df = pd.DataFrame(user_input)
    output = model.predict(input_df)[0]
    return output
