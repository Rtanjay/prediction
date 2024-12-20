import streamlit as st
import pandas as pd

st.title('Prediction with Machine Learning')

st.info('This is a prediction App !')


df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df

