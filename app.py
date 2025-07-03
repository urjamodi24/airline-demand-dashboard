import streamlit as st
import pandas as pd
import plotly.express as px
import cohere
import os
from dotenv import load_dotenv

from fetch_data import (
    fetch_flight_data,
    convert_to_dataframe,
    get_popular_routes,
    get_high_demand_periods,
    get_airline_distribution
)

# -------------------
# Load API Keys
# -------------------
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

# -------------------
# Fetch + Prepare Data
# -------------------
st.title("✈️ Airline Market Demand Dashboard")

with st.spinner("Fetching flight data..."):
    raw_data = fetch_flight_data(limit=100)
    df = convert_to_dataframe(raw_data)

# -------------------
# Filters
# -------------------
origins = ['All'] + sorted(df['departure_iata'].dropna().unique().tolist())
destinations = ['All'] + sorted(df['arrival_iata'].dropna().unique().tolist())

col1, col2 = st.columns(2)
selected_origin = col1.selectbox("Filter by Origin", options=origins)
selected_dest = col2.selectbox("Filter by Destination", options=destinations)

# Apply filters
filtered_df = df.copy()
if selected_origin != "All":
    filtered_df = filtered_df[filtered_df['departure_iata'] == selected_origin]
if selected_dest != "All":
    filtered_df = filtered_df[filtered_df['arrival_iata'] == selected_dest]

st.markdown(f"**Showing {len(filtered_df)} flights**")

# -------------------
# Popular Routes
# -------------------
st.subheader("📍 Popular Routes")
routes_df = get_popular_routes(filtered_df)
fig_routes = px.bar(routes_df.head(10), x='From', y='Count', color='To', title="Top 10 Popular Routes")
st.plotly_chart(fig_routes)

# -------------------
# High Demand Periods
# -------------------
st.subheader("📅 High Demand Dates")
demand_df = get_high_demand_periods(filtered_df)

if demand_df.empty:
    st.info("No valid date data available for high demand chart.")
else:
    fig_demand = px.line(demand_df, x='Date', y='Count', title="Flights per Day")
    st.plotly_chart(fig_demand)

# -------------------
# Airline Distribution
# -------------------
st.subheader("🛫 Flights by Airline")
airline_df = get_airline_distribution(filtered_df)
fig_airline = px.pie(airline_df.head(10), names='Airline', values='Flights', title="Airline Distribution")
st.plotly_chart(fig_airline)

# -------------------
# Raw Data Table (Optional)
# -------------------
with st.expander("🧾 View Raw Flight Data"):
    st.dataframe(filtered_df)

# -------------------
# AI-Powered Insight Summary (Cohere Chat API)
# -------------------
st.subheader("🧠 Insight Summary (AI by Cohere)")

try:
    summary_input = f"""
Popular Routes:
{routes_df.head(5).to_string(index=False)}

High Demand Days:
{demand_df.head(5).to_string(index=False)}

Airline Distribution:
{airline_df.head(5).to_string(index=False)}
"""

    response = co.chat(
        model="command-r",  # or "command-r-plus"
        message=f"Summarize this airline flight data for a business dashboard:\n{summary_input}"
    )

    st.write(response.text.strip())

except Exception as e:
    st.error(f"AI Summary could not be generated: {e}")
