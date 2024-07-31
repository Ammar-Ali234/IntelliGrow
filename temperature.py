import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Inject custom CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get('cod') != '200':
        return None
    return data['list']

def get_weather_icon(icon_code):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    return Image.open(BytesIO(response.content))

def plot_circular_graphs(data):
    df = pd.DataFrame([
        {
            "datetime": item['dt_txt'],
            "temperature": item['main']['temp'],
            "humidity": item['main']['humidity'],
            "rainfall": item.get('rain', {}).get('3h', 0)  # rainfall in the last 3 hours
        }
        for item in data
    ])

    # Calculate the average for circular graphs
    avg_temp = df['temperature'].mean()
    avg_humidity = df['humidity'].mean()
    avg_rainfall = df['rainfall'].mean()

    # Create circular graphs
    fig, axs = plt.subplots(1, 3, figsize=(15, 5), subplot_kw=dict(aspect='equal'))

    # Temperature Circular Graph
    wedges, texts, autotexts = axs[0].pie([avg_temp, 100 - avg_temp], labels=['Temperature', ''], autopct='%1.1f%%', startangle=90, colors=['#ff9999','#e2e2e2'])
    axs[0].set_title('Average Temperature (°C)')
    for autotext in autotexts:
        autotext.set_color('black')

    # Humidity Circular Graph
    wedges, texts, autotexts = axs[1].pie([avg_humidity, 100 - avg_humidity], labels=['Humidity', ''], autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#e2e2e2'])
    axs[1].set_title('Average Humidity (%)')
    for autotext in autotexts:
        autotext.set_color('black')

    # Rainfall Circular Graph
    wedges, texts, autotexts = axs[2].pie([avg_rainfall, 100 - avg_rainfall], labels=['Rainfall', ''], autopct='%1.1f%%', startangle=90, colors=['#99ff99','#e2e2e2'])
    axs[2].set_title('Average Rainfall (mm)')
    for autotext in autotexts:
        autotext.set_color('black')

    plt.tight_layout()
    st.pyplot(fig)

def run_temperature_monitoring():
    st.header("Temperature Monitoring")

    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '1b4b780ecd56b71c78ac99e2549631d4'

    city = st.text_input("Enter city name", "London")
    if st.button("Get Weather"):
        weather_data = get_weather_data(api_key, city)
        if weather_data:
            df = pd.DataFrame([
                {
                    "datetime": item['dt_txt'],
                    "temperature": item['main']['temp'],
                    "humidity": item['main']['humidity'],
                    "rainfall": item.get('rain', {}).get('3h', 0),  # rainfall in the last 3 hours
                    "weather_icon": item['weather'][0]['icon']
                }
                for item in weather_data
            ])
            
            # Display current temperature and weather icon
            current_data = df.iloc[0]  # Use the first data point as current weather
            temp = current_data['temperature']
            icon_code = current_data['weather_icon']
            
            # Show temperature and weather icon
            st.metric(label="Current Temperature", value=f"{temp}°C")
            st.image(get_weather_icon(icon_code), width=100)

            plot_circular_graphs(weather_data)
        else:
            st.error("City not found or API request failed. Please try again.")
