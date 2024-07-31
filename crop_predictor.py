import joblib
import numpy as np
import streamlit as st

def run_crop_predictor():
    # Load the trained model and label encoder
    model = joblib.load('crop_model.pkl')
    label_encoder = joblib.load('label_encoder.pkl')

    # Function to predict crop based on input features
    def predict_crop(temperature, humidity, ph, rainfall):
        # Prepare the input array
        input_features = np.array([[temperature, humidity, ph, rainfall]])
        
        # Predict the label
        label_index = model.predict(input_features)
        
        # Decode the label
        crop_label = label_encoder.inverse_transform(label_index)
        
        return crop_label[0]

    # Streamlit app interface
    st.title('Crop Prediction App')

    st.write("""
    This app predicts the best crop to grow based on the input features.
    """)

    # Get user input
    temperature = st.number_input('Enter temperature:', min_value=-50.0, max_value=50.0, value=25.0)
    humidity = st.number_input('Enter humidity:', min_value=0.0, max_value=100.0, value=50.0)
    ph = st.number_input('Enter pH level:', min_value=0.0, max_value=14.0, value=7.0)
    rainfall = st.number_input('Enter rainfall:', min_value=0.0, max_value=1000.0, value=100.0)

    # Predict button
    if st.button('Predict Crop'):
        predicted_crop = predict_crop(temperature, humidity, ph, rainfall)
        st.write(f'The predicted crop is: {predicted_crop}')

if __name__ == '__main__':
    run_crop_predictor()
