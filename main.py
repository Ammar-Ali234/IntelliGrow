import streamlit as st

# Import feature modules
from disease_classifier import run_disease_classification
from crop_predictor import run_crop_predictor
from temperature import run_temperature_monitoring
from gemini import run_disease_guidance

def main():
    # Inject custom CSS
    css = """
    <style>
    /* General body styling */
    body {
        background-image: url('https://www.wbcsd.org/wp-content/uploads/2023/11/Farmers-stand-to-see-increase-crop-yields-and-profits-with-15-25-return-on-investment-by-transitioning-to-regenerative-farming-practices_i1140-jpg.webp'); /* Background image */
        background-size: cover; /* Cover the entire screen */
        background-position: center; /* Center the background image */
        background-attachment: fixed; /* Keep the background fixed while scrolling */
        color: #013220; /* Green text for readability */
        font-family: 'Arial', sans-serif; /* Font family */
        margin: 0; /* Remove default margins */
        padding: 0; /* Remove default padding */
    }

    /* Overlay for better text visibility */
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5); /* Black overlay with 50% opacity */
        z-index: -1; /* Behind all other elements */
    }

    /* Container styling */
    .stApp {
        background-color: rgba(255, 255, 255, 0.9); /* White background with slight transparency */
        border-radius: 8px; /* Rounded corners */
        padding: 20px; /* Padding around the content */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Light shadow */
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: rgba(255, 68, 51, 0.8); /* #FF4433 background with transparency */
        color: #013220; /* Green text */
        background-image: url('https://www.wbcsd.org/wp-content/uploads/2023/11/Farmers-stand-to-see-increase-crop-yields-and-profits-with-15-25-return-on-investment-by-transitioning-to-regenerative-farming-practices_i1140-jpg.webp'); /* Sidebar background image */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .css-1d391kg::before {
        content: "";
        background: rgba(0, 0, 0, 0.5); /* Black overlay with 50% opacity */
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1; /* Behind all other elements */
    }

    /* Sidebar links */
    .css-1d391kg .stSidebar .stSidebar__menu a {
        color: #013220;
    }

    /* Metric cards styling */
    .css-1lj7l6v {
        background-color: #ffe2df; /* Light background for metrics */
        color: #013220; /* Green text */
        border: 1px solid #013220; /* Green border */
    }

    /* Header styling */
    h1, h2, h3, h4, h5, h6 {
        color: #013220; /* Green headers */
    }

    /* Button styling */
    .stButton button {
        background-color: #013220; /* Green button */
        color: #ffffff; /* White text */
        border: none;
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }

    .stButton button:hover {
        background-color: #013220; /* Darker shade on hover */
    }

    /* Input styling */
    .stTextInput input {
        border: 1px solid #013220; /* Green border */
        border-radius: 4px;
        padding: 10px;
    }

    .stTextInput input:focus {
        border-color: #013220; /* Darker shade on focus */
        outline: none;
    }

    /* File uploader styling */
    .stFileUploader {
        border: 1px solid #013220; /* Green border */
        border-radius: 4px;
        padding: 10px;
        background-color: #ffffff; /* White background */
    }

    .stFileUploader:hover {
        border-color: #013220; /* Darker shade on hover */
    }

    .stFileUploader:focus {
        border-color: #013220; /* Darker shade on focus */
        outline: none;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    # Add overlay for better text visibility
    st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)

    st.title("IntelliGrow: Smart Farming Solution")
    st.sidebar.title("Navigation")

    # Radio buttons for navigation
    option = st.sidebar.radio(
        "Select a Feature",
        ("Home", "Plant Disease Classification", "Crop Prediction", "Temperature Monitoring", "Gemini Chatbot Support")
    )

    if option == "Home":
        st.header("Welcome to IntelliGrow")
        st.write("""
        **IntelliGrow** is a comprehensive smart farming solution designed to help farmers enhance productivity, optimize resource use, and implement sustainable farming practices.
        
        With features such as plant disease classification, crop prediction, temperature monitoring, and disease guidance, IntelliGrow leverages AI and real-time data to provide actionable insights and recommendations.
        
        Explore our features through the navigation menu to learn how IntelliGrow can transform your farming experience.
        """)
    elif option == "Plant Disease Classification":
        st.header("Plant Disease Classification")
        run_disease_classification()
    elif option == "Crop Prediction":
        st.header("Crop Prediction")
        run_crop_predictor()
    elif option == "Temperature Monitoring":
        st.header("Temperature Monitoring")
        run_temperature_monitoring()
    elif option == "Gemini Chatbot Support":
        st.header("Gemini Chatbot Support")
        run_disease_guidance()

if __name__ == "__main__":
    main()
