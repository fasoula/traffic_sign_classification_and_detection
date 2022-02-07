import streamlit as st 
from PIL import Image
import classification
import numpy as np
import base64
from tempfile import NamedTemporaryFile

sign_names = {
        0: 'Speed limit (20km/h)',
        1: 'Speed limit (30km/h)',
        2: 'Speed limit (50km/h)',
        3: 'Speed limit (60km/h)',
        4: 'Speed limit (70km/h)',
        5: 'Speed limit (80km/h)',
        6: 'End of speed limit (80km/h)',
        7: 'Speed limit (100km/h)',
        8: 'Speed limit (120km/h)',
        9: 'No passing',
        10: 'No passing for vehicles over 3.5 metric tons',
        11: 'Right-of-way at the next intersection',
        12: 'Priority road',
        13: 'Yield',
        14: 'Stop',
        15: 'No vehicles',
        16: 'Vehicles over 3.5 metric tons prohibited',
        17: 'No entry',
        18: 'General caution',
        19: 'Dangerous curve to the left',
        20: 'Dangerous curve to the right',
        21: 'Double curve',
        22: 'Bumpy road',
        23: 'Slippery road',
        24: 'Road narrows on the right',
        25: 'Road work',
        26: 'Traffic signals',
        27: 'Pedestrians',
        28: 'Children crossing',
        29: 'Bicycles crossing',
        30: 'Beware of ice/snow',
        31: 'Wild animals crossing',
        32: 'End of all speed and passing limits',
        33: 'Turn right ahead',
        34: 'Turn left ahead',
        35: 'Ahead only',
        36: 'Go straight or right',
        37: 'Go straight or left',
        38: 'Keep right',
        39: 'Keep left',
        40: 'Roundabout mandatory',
        41: 'End of no passing',
        42: 'End of no passing by vehicles over 3.5 metric tons'}

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

main_bg = "route-66.jpg"
main_bg_ext = "jpg"


st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size:cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown("<h1 style='text-align: center; color: gold;'>Traffic Sign Classification</h1>", unsafe_allow_html=True)

button = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: gold;
    color:black;
}
</style>""", unsafe_allow_html=True)



uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg"])

if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)


        st.write("")

        if st.button('predict'):
                label = classification.predict_img(image)
                label = label.argmax()
                res = sign_names.get(label)
                st.markdown(f"<h2 style='text-align: center; font-size: 100px; color: gold;'>{res}</h2>", unsafe_allow_html=True)

