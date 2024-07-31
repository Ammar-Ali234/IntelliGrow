import streamlit as st
from inference_sdk import InferenceHTTPClient
import tempfile
import shutil
import os

def run_disease_classification():
    # Streamlit file uploader to allow only JPG and JPEG formats
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file)
        # Initialize the Roboflow Inference Client
        CLIENT = InferenceHTTPClient(
            api_url="https://outline.roboflow.com",
            api_key="5TOayR5vKledAmbqVwEV"
        )
        
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        
        # Perform inference
        result = CLIENT.infer(temp_file_path, model_id="plant-disease-detection-ryzqa/7")
        
        # Clean up the temporary file
        os.remove(temp_file_path)
        
        # Extract and display results
        if result['predictions']:
            prediction = result['predictions'][0]
            st.write(f"Predicted Class: {prediction['class']}")
            st.write(f"Confidence: {prediction['confidence']:.2f}")
        else:
            st.write("No predictions found.")
