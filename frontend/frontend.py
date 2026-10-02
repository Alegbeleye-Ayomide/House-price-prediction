import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/predict"
st.title('House price predictor')
st.markdown('enter your home specifications below:')

house_age = st.number_input('house age in years', min_value = 1)
GarageCars = st.number_input('GarageCars', min_value = 0)
GarageArea =  st.number_input('GarageArea', min_value = 0)
OverallQual =  st.selectbox('over all quality of the house', options = [1,2,3,4,5,6,7,8,9,10])
OverallCond = st.selectbox('overall condition of the house', options = [1,2,3,4,5,6,7,8,9,10])
Fireplaces = st.number_input('number of fireplaces', min_value = 0)
total_bath = st.number_input('number of bath rooms', min_value = 0)

KitchenQual = st.selectbox('kitchen quality', options = ["Gd", "TA", "Fa", "Ex"])
ExterQual = st.selectbox('Exterior quality', options = ["Gd", "TA", "Fa", "Ex"])
Neighborhood = st.selectbox('Neighbourhood of house', options= ["CollgCr", "Veenker", "Crawfor", "NoRidge", "Mitchel", "Somerst",
            "NWAmes", "OldTown", "BrkSide", "Sawyer", "NAmes", "SawyerW",
            "NridgHt", "IDOTRR", "MeadowV", "Timber", "Gilbert", "ClearCr",
            "Edwards", "NPkVill", "StoneBr", "Blmngtn", "BrDale", "SWISU",
            "Blueste"])
total_sqft = st.number_input('total space of the home in square feet', min_value = 1)


# Assemble payload (ensure key names match Pydantic schema exactly)
input_data = {
    'house_age': house_age,
    'GarageCars': GarageCars,
    'GarageArea': GarageArea,
    'OverallQual': OverallQual,
    'OverallCond': OverallCond,
    'Fireplaces': Fireplaces,
    'total_bath': total_bath,
    'KitchenQual': KitchenQual,
    'ExterQual': ExterQual,
    'Neighborhood': Neighborhood,  
    'total_sqft': total_sqft,      
}

# Ensure st.button triggers the request
if st.button("Predict Price"):
    input_data = {
    'house_age': house_age,
    'GarageCars': GarageCars,
    'GarageArea': GarageArea,
    'OverallQual': OverallQual,
    'OverallCond': OverallCond,
    'Fireplaces': Fireplaces,
    'total_bath': total_bath,
    'KitchenQual': KitchenQual,
    'ExterQual': ExterQual,
    'Neighborhood': Neighborhood,  #
    'total_sqft': total_sqft,      
}

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Price: ${result['predicted_price']:,.2f}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to the FastAPI server: {e}")

