import streamlit as st
import numpy as np
import pickle

with open('C:/Users/prudh/OneDrive/Desktop/Machine Learning/Projects/Big Mart Sales Prediction/big_mart.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.set_page_config(page_title="Big Mart Sales Predictor", layout="centered")
st.title("Big Mart Sales Prediction")

item_identifier = st.selectbox("Item Identifier", ['FDA15', 'DRC01', 'FDN15', 'FDQ58', 'FDP36'])
item_weight = st.number_input("Item Weight", min_value=0.0, format="%.2f")
item_visibility = st.number_input("Item Visibility", min_value=0.0, format="%.6f")
item_mrp = st.number_input("Item MRP", min_value=0.0, format="%.2f")

item_fat_content = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
item_type = st.selectbox("Item Type", ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household',
                                       'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene',
                                       'Hard Drinks', 'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood'])
outlet_identifier = st.selectbox("Outlet Identifier", ['OUT049', 'OUT018', 'OUT010', 'OUT013', 'OUT027',
                                                       'OUT045', 'OUT017', 'OUT046', 'OUT035', 'OUT019'])
outlet_establishment_year = st.number_input("Outlet Establishment Year", min_value=1985, max_value=2025, step=1)
outlet_size = st.selectbox("Outlet Size", ['Small', 'Medium', 'High'])
outlet_location_type = st.selectbox("Outlet Location Type", ['Tier 1', 'Tier 2', 'Tier 3'])
outlet_type = st.selectbox("Outlet Type", ['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'])

def encode(val, categories):
    return categories.index(val)

if st.button("Predict Sales"):
    input_data = np.array([[
        encode(item_identifier, ['FDA15', 'DRC01', 'FDN15', 'FDQ58', 'FDP36']),
        item_weight,
        item_visibility,
        item_mrp,
        encode(item_fat_content, ['Low Fat', 'Regular']),
        encode(item_type, ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household',
                           'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene',
                           'Hard Drinks', 'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood']),
        encode(outlet_identifier, ['OUT049', 'OUT018', 'OUT010', 'OUT013', 'OUT027',
                                   'OUT045', 'OUT017', 'OUT046', 'OUT035', 'OUT019']),
        outlet_establishment_year,
        encode(outlet_size, ['Small', 'Medium', 'High']),
        encode(outlet_location_type, ['Tier 1', 'Tier 2', 'Tier 3']),
        encode(outlet_type, ['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'])
    ]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Sales: ₹ {prediction:.2f}")
