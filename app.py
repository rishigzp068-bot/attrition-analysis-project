import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Palo Alto Networks.xlsx")

# Convert correctly
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

st.title("Employee Attrition Dashboard")

# ---------------- Department Chart ----------------
st.subheader("Attrition by Department")

dept = df.groupby("Department")["Attrition"].mean() * 100

fig, ax = plt.subplots()
dept.plot(kind="bar", ax=ax, color="skyblue")  # IMPORTANT FIX
ax.set_ylabel("Attrition %")

st.pyplot(fig)
