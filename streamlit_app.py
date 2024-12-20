import streamlit as st
import pandas as pd

st.title('Prediction with Machine Learning')

st.info('This is a prediction App !')


with st.expander("Data"):
  st.write("**Raw Data** :")
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write("**Y**")
  # species
  y = df["species"]
  y
  
  st.write("**X**")
  # Columns in Data set: "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  x = df.drop("species", axis=1, inplace = False)
  x

with st.expander("Data Visualisations ! "):
  
  st.scatter_chart(data = df, x = "bill_length_mm" , y = "body_mass_g", color = "species")

# Data Preparations:

with st.sidebar:
  st.header("Input features")

  island = st.selectbox('Islands' , ('Torgersen', 'Biscoe', 'Dream'))
  gender = st.selectbox('Gender' , ('Male', 'Female'))

  bill_len_mm = st.slider('Bill Length (mm)' , 32.1 , 59.64 , 43.9)
  bill_depth_mm = st.slider('Bill Depth (mm)' , 13.1 , 21.5 , 17.2)
  flipper_length_mm = st.slider('Flipper Length (mm)' , 172.0 , 230.0 , 201.0)

