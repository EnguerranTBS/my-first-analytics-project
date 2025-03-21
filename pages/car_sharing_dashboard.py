import streamlit as st
import pandas as pd

# Function to load CSV files into dataframes
@st.cache_data
def load_data():
    trips = pd.read_csv("datasets/trips.csv")
    cars = pd.read_csv("datasets/cars.csv")
    cities = pd.read_csv("datasets/cities.csv")
    return trips, cars, cities

# Load data
trips, cars, cities = load_data()

trips_merged = trips.merge(cars, on="car_id", how="left")

trips_merged = trips_merged.merge(cities, on="city_id", how="left")

trips_merged = trips_merged.drop(columns=["car_id", "city_id", "customer_id", "id"])

