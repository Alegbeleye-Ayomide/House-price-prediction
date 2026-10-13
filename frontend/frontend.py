import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="House Price Predictor", page_icon="🏠")
st.title(" House Price Predictor")
st.markdown("Enter property details below to calculate an estimated price:")

# Grid layout for inputs
col1, col2 = st.columns(2)

with col1:
    LotArea = st.number_input(
        "Lot Area (sq ft)", min_value=100.0, value=8450.0, step=100.0
    )
    total_sqft = st.number_input(
        "Total Space (sq ft)", min_value=100.0, value=1710.0, step=50.0
    )
    house_age = st.number_input(
        "House Age (years)", min_value=0.0, value=20.0, step=1.0
    )
    GarageCars = st.number_input(
        "Garage Capacity (cars)", min_value=0, value=2, step=1
    )
    KitchenAbvGr = st.number_input(
        "Kitchens Above Ground", min_value=1, value=1, step=1
    )

with col2:
    OverallQual = st.selectbox(
        "Overall Quality (1-10)", options=list(range(1, 11)), index=6
    )
    OverallCond = st.selectbox(
        "Overall Condition (1-10)", options=list(range(1, 11)), index=4
    )
    total_bath = st.number_input(
        "Total Bathrooms", min_value=0.0, value=2.5, step=0.5
    )
    MSZoning = st.selectbox(
        "MS Zoning", options=["RL", "RM", "FV", "RH", "C (all)"]
    )
    Neighborhood = st.selectbox(
        "Neighborhood",
        options=[
            "Blueste",
            "BrDale",
            "BrkSide",
            "ClearCr",
            "CollgCr",
            "Crawfor",
            "Edwards",
            "Gilbert",
            "IDOTRR",
            "MeadowV", "Mitchel",
            "NAmes",
            "NPkVill",
            "NWAmes",
            "NoRidge",
            "NridgHt",
            "OldTown",
            "SWISU",
            "Sawyer",
            "SawyerW",
            "Somerst",
            "StoneBr",
            "Timber",
            "Veenker",
        ],
    )

st.markdown("---")

if st.button("Predict Price", type="secondary"):
    # Payload keys match FastAPI backend schema exactly
    input_data = {
        "LotArea": LotArea,
        "OverallQual": OverallQual,
        "OverallCond": OverallCond,
        "KitchenAbvGr": KitchenAbvGr,
        "GarageCars": GarageCars,
        "house_age": house_age,
        "total_sqft": total_sqft,
        "total_bath": total_bath,
        "MSZoning": MSZoning,
        "Neighborhood": Neighborhood,
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"### Predicted Price: **${result['predicted_price']:,.2f}**")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to the FastAPI server: {e}")