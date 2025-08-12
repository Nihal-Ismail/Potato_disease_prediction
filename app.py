import os
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import time
import base64
from io import BytesIO
from styles import apply_styles  # keep your same styles file

# ✅ Must be first Streamlit command
st.set_page_config(
    page_title="Potato Disease Classifier",
    page_icon="🥔",
    layout="centered"
)

# --------- Class Labels, Styles & Icons ---------
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
CLASS_TO_CSS = {
    "Early Blight": "early",
    "Late Blight": "late",
    "Healthy": "healthy"
}
CLASS_ICONS = {
    "Early Blight": "🍂",
    "Late Blight": "🧡",
    "Healthy": "🌱"
}

# --------- Apply Styles ---------
apply_styles(st)

# --------- Model Loading ---------
@st.cache_resource
def load_model():
    model_path = "potato_disease_classification_model.h5"
    return tf.keras.models.load_model(model_path)

model = load_model()

# --------- Image Preprocessing ---------
def preprocess_image(image: Image.Image):
    image = image.resize((256, 256))
    img_array = tf.keras.utils.img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

# --------- UI Title ---------
st.markdown("<h1 style='text-align: center;'>🥔 Potato Disease Classifier</h1>", unsafe_allow_html=True)
st.write("Upload a potato leaf image to identify if it has Early Blight, Late Blight, or is Healthy.")

# --------- File Upload ---------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        with st.spinner("Analyzing the leaf..."):
            time.sleep(1)  # just to simulate loading
            processed_image = preprocess_image(image)
            predictions = model.predict(processed_image)
            score = tf.nn.softmax(predictions[0])
            predicted_class = CLASS_NAMES[np.argmax(score)]
            confidence = 100 * np.max(score)

        css_class = CLASS_TO_CSS[predicted_class]
        icon = CLASS_ICONS[predicted_class]

        st.markdown(
            f"<h2 class='{css_class}'>Prediction: {predicted_class} {icon}</h2>",
            unsafe_allow_html=True
        )
        st.write(f"Confidence: **{confidence:.2f}%**")
