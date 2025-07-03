import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

BASE_URL = "http://api.aviationstack.com/v1/flights"

# -----------------------
# 1. Fetch Raw Data
# -----------------------
def fetch_flight_data(limit=100):
    params = {
        "access_key": API_KEY,
        "limit": limit
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status: {response.status_code}")
    
    data = response.json()
    return data.get("data", [])  # safe fallback if "data" key is missing

# -----------------------
# 2. Convert to DataFrame
# -----------------------
def convert_to_dataframe(flight_data):
    records = []

    for item in flight_data:
        try:
            records.append({
                "departure_airport": item["departure"]["airport"],
                "departure_iata": item["departure"]["iata"],
                "arrival_airport": item["arrival"]["airport"],
                "arrival_iata": item["arrival"]["iata"],
                "airline": item["airline"]["name"],
                "flight_date": item["flight_date"],
                "status": item["flight_status"]
            })
        except (TypeError, KeyError):
            continue  # skip any malformed entries

    return pd.DataFrame(records)

# -----------------------
# 3. Analytics Functions
# -----------------------
def get_popular_routes(df):
    route_counts = df.groupby(["departure_iata", "arrival_iata"]).size().reset_index(name='Count')
    route_counts.columns = ['From', 'To', 'Count']
    return route_counts.sort_values(by='Count', ascending=False)

def get_high_demand_periods(df):
    # Step 1: Remove empty or null date strings
    df = df[df['flight_date'].notnull() & (df['flight_date'] != '')]

    # Step 2: Convert to datetime
    df["flight_date"] = pd.to_datetime(df["flight_date"], errors='coerce')

    # Step 3: Drop rows where conversion failed
    df = df.dropna(subset=["flight_date"])

    if df.empty:
        return pd.DataFrame(columns=["Date", "Count"])

    # Step 4: Extract date and count
    df['day'] = df['flight_date'].dt.date
    daily_flights = df.groupby("day").size().reset_index(name='Count')
    daily_flights.columns = ['Date', 'Count']
    return daily_flights.sort_values(by='Count', ascending=False)



def get_airline_distribution(df):
    airline_counts = df["airline"].value_counts().reset_index()
    airline_counts.columns = ['Airline', 'Flights']
    return airline_counts
