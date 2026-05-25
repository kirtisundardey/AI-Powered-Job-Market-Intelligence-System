import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('data/processed/cleaned_jobs.csv')

# Title
st.title("AI-Powered Job Market Intelligence Dashboard")

# KPI Metrics
st.metric("Total Jobs", len(df))
st.metric("Average Salary", round(df['Salary_Avg'].mean(), 2))
st.metric("Top City", df['Job_City'].mode()[0])

# Sidebar filter
st.sidebar.header("Filters")

selected_city = st.sidebar.selectbox(
    "Select City",
    df['Job_City'].unique()
)

filtered_df = df[
    df['Job_City'] == selected_city
]

# Salary Distribution
fig1 = px.histogram(
    filtered_df,
    x='Salary_Avg',
    nbins=20,
    title='Salary Distribution'
)

st.plotly_chart(fig1)

# Top Companies
company_counts = filtered_df['Company_Name'].value_counts().head(10)

fig2 = px.bar(
    x=company_counts.index,
    y=company_counts.values,
    title='Top Hiring Companies'
)

st.plotly_chart(fig2)