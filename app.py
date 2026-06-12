import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE ----------------
st.set_page_config(page_title="Attrition Dashboard", layout="wide")
st.title("📊 Employee Attrition Dashboard")

# ---------------- LOAD DATA ----------------
df = pd.read_excel("Palo Alto Networks.xlsx")

# ---------------- CLEAN DATA ----------------
df['Attrition'] = df['Attrition'].astype(str).str.strip().str.title()
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df['Attrition'] = df['Attrition'].fillna(0).astype(int)

# ---------------- KPI ----------------
attrition_rate = df['Attrition'].mean() * 100

col1, col2 = st.columns(2)
col1.metric("Total Employees", len(df))
col2.metric("Attrition Rate (%)", round(attrition_rate, 2))

st.divider()

# ---------------- TABLE ----------------
st.subheader("Raw Data")
st.dataframe(df)

st.divider()

# ---------------- DEPARTMENT WISE ----------------
st.subheader("Attrition by Department")

dept = df.groupby("Department")["Attrition"].mean() * 100

fig, ax = plt.subplots()
ax.bar(dept.index, dept.values, color="skyblue")
ax.set_ylabel("Attrition %")
ax.set_xlabel("Department")

st.pyplot(fig)

st.divider()

# ---------------- JOB ROLE WISE ----------------
st.subheader("Attrition by Job Role")

role = df.groupby("JobRole")["Attrition"].mean() * 100

fig2, ax2 = plt.subplots()
ax2.bar(role.index, role.values, color="orange")
ax2.set_ylabel("Attrition %")
ax2.set_xlabel("Job Role")
plt.xticks(rotation=45)

st.pyplot(fig2)

st.divider()

# ---------------- DOWNLOAD REPORT ----------------
report = df.copy()

csv = report.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download Full Dataset",
    data=csv,
    file_name="attrition_report.csv",
    mime="text/csv"
)
