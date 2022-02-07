from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import streamlit as st
import cv2
from PIL import Image

@st.cache(allow_output_mutation=True)
def get_model():
        model = load_model('traffic_signsv2.h5')
        print('Model Loaded')
        return model 

        
def predict_img(image):
        loaded_model = get_model()
        image = image.resize((28,28), Image.ANTIALIAS)
        image = np.array(image)
        image = np.reshape(image,[1,28,28,3])

        classes = loaded_model.predict(image)

        return classes
