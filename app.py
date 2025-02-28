import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('Banglore_traffic_Dataset (1).csv')

data = load_data()

# Dashboard Title
st.title("🚦 Bangalore Traffic Analysis Dashboard")
st.markdown("""
Analyze Bangalore's traffic patterns to provide insights for better urban traffic management.
""")

# Data Overview
st.header("📊 Traffic Data Overview")
st.dataframe(data.head())

# Traffic Volume by Area
st.header("📈 Traffic Volume by Area")
area = st.selectbox("Select an Area", data["Area Name"].unique())
filtered_data = data[data["Area Name"] == area]
fig = px.bar(filtered_data, x="Road/Intersection Name", y="Traffic Volume", color="Congestion Level", title=f"Traffic in {area}")
st.plotly_chart(fig)

# Average Speed Distribution
st.header("🚗 Average Speed Distribution")
speed_fig = px.histogram(data, x="Average Speed", nbins=30, title="Distribution of Vehicle Speed")
st.plotly_chart(speed_fig)

# Congestion Level Comparison
st.header("🔎 Compare Congestion Levels")
compare_areas = st.multiselect("Select Areas", data["Area Name"].unique(), default=data["Area Name"].unique()[:3])
compare_data = data[data["Area Name"].isin(compare_areas)]
congestion_fig = px.line(compare_data, x="Road/Intersection Name", y="Congestion Level", color="Area Name", title="Congestion Across Areas")
st.plotly_chart(congestion_fig)

# Environmental Impact
st.header("🌳 Environmental Impact")
impact_fig = px.scatter(data, x="Traffic Volume", y="Environmental Impact", color="Area Name", title="Traffic vs. Environmental Impact")
st.plotly_chart(impact_fig)

# Summary
st.markdown("### 📌 Insights:")
st.write("""
1. Identify high-traffic zones for better traffic management.
2. Correlate traffic congestion with environmental impact.
3. Use insights to optimize public transport and reduce congestion.
""")
