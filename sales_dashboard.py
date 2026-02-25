import pandas as pd
import streamlit as st
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Sales Performance Tracker", layout="wide")

# 2. Data Loading with Caching
@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv")
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    # Convert period to string for Plotly compatibility
    df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
    # Ensure Customer_ID is treated as a category
    df['Customer_ID'] = df['Customer_ID'].astype(str)
    return df

df = load_data()

# 3. Sidebar Interactivity
st.sidebar.header("🔍 Global Filters")
selected_region = st.sidebar.multiselect(
    "Select Region(s):",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

# Apply Filter
filtered_df = df[df["Region"].isin(selected_region)]

# 4. Header Section
st.title("📊 Sales Performance Dashboard")
st.markdown("Analyze revenue trends, regional performance, and customer value.")

# 5. KPI Metrics Row
total_rev = filtered_df['Revenue'].sum()
total_prof = filtered_df['Profit'].sum()
margin = (total_prof / total_rev * 100) if total_rev != 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"${total_rev:,.2f}")
col2.metric("📈 Total Profit", f"${total_prof:,.2f}")
col3.metric("🎯 Profit Margin", f"{margin:.1f}%")

st.divider()

# 6. Charts Layout (2x2 Grid)
row1_left, row1_right = st.columns(2)
row2_left, row2_right = st.columns(2)

with row1_left:
    st.subheader("Monthly Revenue Trend")
    monthly_data = filtered_df.groupby('Month')['Revenue'].sum().reset_index()
    fig1 = px.line(monthly_data, x='Month', y='Revenue', markers=True, template="plotly_white")
    st.plotly_chart(fig1, width="stretch")

with row1_right:
    st.subheader("Revenue by Region")
    region_rev = filtered_df.groupby('Region')['Revenue'].sum().reset_index()
    fig2 = px.bar(region_rev, x='Region', y='Revenue', color='Region', text_auto='.2s')
    st.plotly_chart(fig2, width="stretch")

with row2_left:
    st.subheader("Top 5 Customers by Revenue")
    top_cust = filtered_df.groupby('Customer_ID')['Revenue'].sum().nlargest(5).reset_index()
    fig3 = px.bar(top_cust, x='Customer_ID', y='Revenue', color='Revenue', color_continuous_scale="Viridis")
    st.plotly_chart(fig3, width="stretch")

with row2_right:
    st.subheader("Profit by Region")
    region_prof = filtered_df.groupby('Region')['Profit'].sum().reset_index()
    fig4 = px.bar(region_prof, x='Region', y='Profit', color='Region', pattern_shape="Region")
    st.plotly_chart(fig4, width="stretch")