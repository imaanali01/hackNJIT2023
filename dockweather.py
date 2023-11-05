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
st.markdown('<style>' + open('custom.css').read() + '</style>', unsafe_allow_html=True)

# Sidebar widgets for Dock Weather
st.sidebar.image(image_url)
st.sidebar.header("Dock Weather App")

# Create a sidebar navigation
page = st.sidebar.selectbox("Select a page", ["Home", "About"])

if page == "Home":
    # Home page content
    city = st.sidebar.text_input("Enter City Name", "New York")
    units = st.sidebar.selectbox("Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)"])
    show_weather = st.sidebar.checkbox("Show Weather", value=True)

    # Main content for Dock Weather
    st.title("Dock Weather PRO")

    if show_weather:
        if st.button("Get Weather"):
            weather_data = get_weather_data(city, units, API_KEY)
                
            # Create a layout with three columns
            col1, col2, col3 = st.columns(3)
            
            # Place a logo at the top of each column
            with col1:
                st.image("https://www.creativefabrica.com/wp-content/uploads/2019/02/Earth-icon-by-rudezstudio-1-580x386.jpg")
                if weather_data:
                    st.write(f'<div style="text-align: center;">Location: {city}</div>', unsafe_allow_html=True)
            
            with col2:
                st.write("")
                left_co, cent_co,last_co = st.columns(3)
                with cent_co:
                    st.image("https://www.pngall.com/wp-content/uploads/2017/01/Temperature-PNG-Clipart.png", width=100)
                    st.write("")
                    st.write("")
                st.write(f'<div style="text-align: center;">Temperature: {weather_data['main']['temp']} {units[0]}</div>', unsafe_allow_html=True)
            
            with col3:
                st.write("")
                if 'weather' in weather_data:
                    weather_condition = weather_data['weather'][0]['main']
                    left_co, cent_co,last_co = st.columns(3)
                    with cent_co:
                        if weather_condition == 'Clear':
                            st.image("https://cdn1.iconfinder.com/data/icons/weather-forecast-meteorology-color-1/128/weather-sunny-512.png", width=100)
                        elif weather_condition == 'Clouds':
                            st.image("https://visualpharm.com/assets/942/Clouds-595b40b65ba036ed117d3942.svg", width=100)
                        elif weather_condition == 'Rain':
                            st.image("https://cdn1.vectorstock.com/i/1000x1000/59/60/rain-cloud-icon-line-raindrop-symbol-vector-21085960.jpg", width=100)
                st.write("")
                st.write("")
                st.write(f'<div style="text-align: center;">Conditions: {weather_data['weather'][0]['description']}</div>', unsafe_allow_html=True)
                

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    if st.button("Detailed Condition Alert"):
        st.subheader("Marinetime statement for dock workers:")
        st.write('''Sample Marine Weather Statement: 
                
        FZUS71 KOKX 301602 MWSOKX 
        Marine Weather Statement National Weather Service New York 
        NY 1202 PM EDT Mon Oct 30 2023
        ANZ345-350-353-355-301900-South Shore Bays from Jones Inlet through Shinnecock Bay-
        Moriches Inlet NY to Montauk Point NY out 20 nm-
        Fire Island Inlet NY to Moriches Inlet NY out 20 nm-
        Sandy Hook NJ to Fire Island Inlet NY out 20 nm-
        1202 PM EDT Mon Oct 30 2023

        ...Locally Dense Fog...

        Locally dense fog with visibilities 1 nm or less are possible
        this afternoon. Reduce your speed, and keep a lookout for other
        vessels, buoys, and breakwaters. Keep your navigation lights on.
        If not equipped with radar, you should consider seeking safe
        harbor.

        ANZ340-301900-
        Peconic and Gardiners Bays-
        1202 PM EDT Mon Oct 30 2023

        ...Locally Dense Fog...

        Locally dense fog with visibilities 1 nm or less are possible
        this afternoon. Reduce your speed, and keep a lookout for other
        vessels, buoys, and breakwaters. Keep your navigation lights on.
        If not equipped with radar, you should consider seeking safe
        harbor.
        ''')

elif page == "About":
    # About page content
    st.title("About Dock Worker PRO")
    st.write("This is the about page for Dock Worker PRO.")
    # Add more content or information about your app here

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Created by Imaan A")

# Run the app
if __name__ == "__main__":
    st.write("This is a Streamlit app for dock workers to access weather and other critical information regarding marinetime conditions.")
