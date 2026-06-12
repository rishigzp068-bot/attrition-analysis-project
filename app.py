import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Attrition Dashboard", layout="wide")
st.title("📊 Employee Attrition Analysis Dashboard")

# ---------------- LOAD DATA ----------------
df = pd.read_excel("Palo Alto Networks.xlsx")

# ---------------- CLEAN COLUMN NAMES ----------------
df.columns = df.columns.str.strip()

# ---------------- SAFETY CHECK ----------------
st.write("Columns:", df.columns)

# ---------------- CLEAN ATTRITION ----------------
df["Attrition"] = df["Attrition"].astype(str).str.strip().str.lower()

df["Attrition"] = df["Attrition"].replace({
    "yes": 1,
    "no": 0
})

df["Attrition"] = pd.to_numeric(df["Attrition"], errors="coerce")
df["Attrition"] = df["Attrition"].fillna(0).astype(int)

# ---------------- DEBUG ----------------
st.write("Attrition values:", df["Attrition"].value_counts())

# ---------------- KPI ----------------
attrition_rate = df["Attrition"].mean() * 100

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
    st.error("Department column missing")

st.divider()

# ---------------- JOB ROLE CHART ----------------
st.subheader("Attrition by Job Role")

if "JobRole" in df.columns:
    role = df.groupby("JobRole")["Attrition"].mean() * 100
    role = role.dropna()

    fig2, ax2 = plt.subplots()
    ax2.bar(role.index.astype(str), role.values, color="orange")
    plt.xticks(rotation=45)

    st.pyplot(fig2)
else:
    st.error("JobRole column missing")

st.divider()

# ---------------- DOWNLOAD ----------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Clean Dataset",
    data=csv,
    file_name="attrition_clean_data.csv",
    mime="text/csv"
)
