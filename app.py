import streamlit as st
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from styles import apply_styles

# Apply custom UI styles
apply_styles(st)

# Cache model so it loads only once
@st.cache_resource(show_spinner=False)
def load_model():
    model_path = os.path.join("saved_models", "1")
    return tf.saved_model.load(model_path).signatures["serving_default"]

model = load_model()

# Prediction function
def predict(image: Image.Image):
    img = image.resize((256, 256))  # match training input size
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model(tf.constant(img_array))
    predicted_class = np.argmax(list(prediction.values())[0].numpy(), axis=1)[0]

    labels = ["Early Blight", "Late Blight", "Healthy"]
    return labels[predicted_class]

# Streamlit app
st.title("🌿 Potato Disease Detection")
uploaded_file = st.file_uploader("Upload a potato leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    with st.spinner("Analyzing leaf..."):
        result = predict(image)

    st.success(f"✅ Prediction: **{result}**")
