import streamlit as st
import pandas as pd

st.title('Prediction with Machine Learning')

st.info('This is a prediction App !')


with st.expander("Data"):
  st.write("**Raw Data** :")
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write("**X**")
  x = df.drop("species", axis=1, inplace = False)
  x

  st.write("**Y**")
  y = df("species")
  y
