import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE ----------------
st.set_page_config(page_title="Attrition Dashboard", layout="wide")
st.title("📊 Employee Attrition Dashboard")

# ---------------- LOAD DATA ----------------
df = pd.read_excel("Palo Alto Networks.xlsx")

# ---------------- CHECK COLUMNS (DEBUG SAFETY) ----------------
st.write("Columns in dataset:", df.columns)

# ---------------- CLEAN COLUMN NAMES ----------------
df.columns = df.columns.str.strip()

# ---------------- CLEAN ATTRITION ----------------
df['Attrition'] = df['Attrition'].astype(str).str.strip().str.lower()

df['Attrition'] = df['Attrition'].map({
    'yes': 1,
    'no': 0
})

df['Attrition'] = df['Attrition'].fillna(0).astype(int)

# ---------------- FINAL CHECK ----------------
st.write("Attrition value counts:", df['Attrition'].value_counts())

# ---------------- KPI ----------------
attrition_rate = df['Attrition'].mean() * 100

col1, col2 = st.columns(2)
col1.metric("Total Employees", len(df))
col2.metric("Attrition Rate (%)", round(attrition_rate, 2))

st.divider()

# ---------------- RAW DATA ----------------
st.subheader("Dataset Preview")
st.dataframe(df)

st.divider()

# ---------------- DEPARTMENT CHART ----------------
st.subheader("Attrition by Department")

if "Department" in df.columns:

    dept = df.groupby("Department")["Attrition"].mean() * 100
    dept = dept.dropna()

    fig, ax = plt.subplots()
    ax.bar(dept.index.astype(str), dept.values, color="skyblue")
    ax.set_ylabel("Attrition %")
    ax.set_xlabel("Department")

    st.pyplot(fig)

else:
    st.error("Department column not found")

st.divider()

# ---------------- JOB ROLE CHART ----------------
st.subheader("Attrition by Job Role")

if "JobRole" in df.columns:

    role = df.groupby("JobRole")["Attrition"].mean() * 100
    role = role.dropna()

    fig2, ax2 = plt.subplots()
    ax2.bar(role.index.astype(str), role.values, color="orange")
    ax2.set_ylabel("Attrition %")
    ax2.set_xlabel("Job Role")
    plt.xticks(rotation=45)

    st.pyplot(fig2)

else:
    st.error("JobRole column not found")

st.divider()

# ---------------- DOWNLOAD ----------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Clean Dataset",
    data=csv,
    file_name="attrition_clean_data.csv",
    mime="text/csv"
)
