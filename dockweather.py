import streamlit as st
import requests

# Streamlit configuration
st.set_page_config(
    page_title="Dock Worker PRO",
    layout="wide"
)

# API configuration
API_KEY = "a6f91d29243a65eecfcabe64be76c90f"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Sidebar widgets
st.sidebar.header("Dock Worker App")
city = st.sidebar.text_input("Enter City Name", "New York")
units = st.sidebar.selectbox("Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)"])
show_weather = st.sidebar.checkbox("Show Weather", value=True)
show_other_info = st.sidebar.checkbox("Show Other Information", value=True)

# Function to fetch weather data
def get_weather_data(city, units, api_key):
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

# Main content
st.title("Dock Worker Information")
weather_data = get_weather_data(city, units, API_KEY)

if show_weather and weather_data:
    st.header(f"Weather in {city}")
    st.subheader(f"Temperature: {weather_data['main']['temp']} {units[0]}")
    st.subheader(f"Description: {weather_data['weather'][0]['description']}")

if show_other_info:
    st.header("Other Information for Dock Workers")
    # You can add more information here.

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Created by Your Name")

# Run the app
if __name__ == "__main__":
    st.write("This is a Streamlit app for dock workers to access weather and other information.")
