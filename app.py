import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Employee Attrition Dashboard")

df = pd.read_excel("Palo Alto Networks.xlsx")

# Convert Attrition
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# ---------------- KPI ----------------
attrition_rate = df['Attrition'].mean() * 100

st.metric("Attrition Rate (%)", round(attrition_rate, 2))

# ---------------- TABLE ----------------
st.subheader("Raw Data")
st.dataframe(df)

# ---------------- CHART 1 ----------------
st.subheader("Attrition by Department")

dept = df.groupby("Department")["Attrition"].mean() * 100

fig, ax = plt.subplots()
dept.plot(kind="bar", ax=ax)
st.pyplot(fig)

# ---------------- CHART 2 ----------------
st.subheader("Attrition by Gender")

gender = df.groupby("Gender")["Attrition"].mean() * 100

fig2, ax2 = plt.subplots()
gender.plot(kind="bar", ax=ax2)
st.pyplot(fig2)
