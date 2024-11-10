import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Define column names
X_Name = 'Diameter (inches)'
y_name = 'Price (USD)'

# Load data
df = pd.read_csv('./data/pizza_data.csv')

# Initialize and train model
model = LinearRegression()
x = df[[X_Name]]  # Reshape to 2D by using double brackets
y = df[y_name]

model.fit(x, y)

# Streamlit app
st.title('Data Prediction')
st.divider()

# Input for pizza diameter
diameter = st.number_input("Type the Pizza Diameter:")

# Prediction
if diameter != 0:
    price = model.predict([[diameter]])[0]
    st.write(f"The pizza value with diameter {diameter:.2f} is: R${price:.2f}")
