from fetch_data import fetch_flight_data, convert_to_dataframe, get_popular_routes, get_high_demand_periods

data = fetch_flight_data(100)
df = convert_to_dataframe(data)

print("\nPopular Routes:")
print(get_popular_routes(df).head())

print("\nHigh Demand Days:")
print(get_high_demand_periods(df).head())
