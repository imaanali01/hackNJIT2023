import streamlit as st
import requests
import os
import json

# Set the OpenWeatherMap API key
os.environ["OPENWEATHER_API_KEY"] = "a6f91d29243a65eecfcabe64be76c90f"

# Function to fetch weather data
def get_weather_data(city, units, api_key):
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "imperial" if units == "Fahrenheit (°F)" else "metric",
        "appid": api_key,
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Streamlit configuration
st.set_page_config(
    page_title="Dock Worker PRO",
    layout="wide"
)

# API configuration
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if API_KEY is None:
    st.error("Please set your OpenWeatherMap API key as an environment variable (OPENWEATHER_API_KEY).")
    st.stop()

# Load image URL from JSON file
with open("image.json", "r") as config_file:
    config_data = json.load(config_file)
image_url = config_data.get("image_url", "")

# Add custom CSS styles to change sidebar color
with open('custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar widgets for Dock Weather
st.sidebar.image(image_url)
st.sidebar.header("Dock Weather PRO")
city = st.sidebar.text_input("Enter City Name", "New York")
units = st.sidebar.selectbox("Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)"])
show_weather = st.sidebar.checkbox("Show Weather", value=True)
show_other_info = st.sidebar.checkbox("Show Other Information", value=True)

# Main content for Dock Weather
st.title("Dock Weather PRO")

if show_weather:
    if st.button("Get Weather"):
        weather_data = get_weather_data(city, units, API_KEY)
        if weather_data:
            st.header(f"Weather in {city}")
            st.subheader(f"Temperature: {weather_data['main']['temp']} {units[0]}")
            st.subheader(f"Description: {weather_data['weather'][0]['description']}")
            st.subheader("Conditions seem to be optimal for port activity today!")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Created by Imaan A")

# Run the app
if __name__ == "__main__":
    st.write("This is a Streamlit app that provides weather and sea condition information to dock workers.")
