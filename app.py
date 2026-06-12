import streamlit as st
import pandas as pd

st.title("Employee Attrition Dashboard")

df = pd.read_excel("Palo Alto Networks.xlsx")

st.write(df)
