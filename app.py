import streamlit as st
import numpy as np
from PIL import Image
import time
import base64
from io import BytesIO
from styles import apply_styles

# ----------------------------
# Page Config & Styles
# ----------------------------
st.set_page_config(page_title="Potato Disease Classifier", page_icon="🥔", layout="centered")
apply_styles(st)

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

@st.cache_resource
def load_model():
    from keras.layers import TFSMLayer
    from keras import Input, Model
    base_model = TFSMLayer("C:/potato_disease/saved_models/1", call_endpoint="serving_default")
    input_layer = Input(shape=(None, None, 3))
    output = base_model(input_layer)
    model = Model(inputs=input_layer, outputs=output)
    return model

try:
    MODEL = load_model()
except Exception as e:
    st.error(f"❗ Model loading failed: {str(e)}")
    MODEL = None

def image_to_base64(img_array):
    img = Image.fromarray(img_array.astype('uint8'))
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def read_image(image_file):
    try:
        image = Image.open(image_file).convert("RGB")
        return np.array(image)
    except Exception as e:
        st.error(f"Image loading failed: {str(e)}")
        return None

# ----------------------------
# UI
# ----------------------------
st.markdown('<div class="main-title">🥔 Potato Disease Classifier</div>', unsafe_allow_html=True)
st.write("Upload a clear potato plant leaf image to detect health and disease type.")
st.markdown('<hr />', unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_np = read_image(uploaded_file)
    if image_np is not None:
        img_b64 = image_to_base64(image_np)
        st.markdown(
            f"<img src='data:image/png;base64,{img_b64}' class='image-preview'/>",
            unsafe_allow_html=True
        )

        with st.spinner("Analyzing ..."):
            time.sleep(1.2)  # Simulate processing
            img_batch = np.expand_dims(image_np, 0)

            if MODEL is None:
                st.error("Model not loaded. Cannot make predictions.")
            else:
                try:
                    predictions = MODEL.predict(img_batch)
                    if isinstance(predictions, dict):
                        predictions = list(predictions.values())[0]

                    class_idx = int(np.argmax(predictions[0]))
                    predicted_class = CLASS_NAMES[class_idx]
                    confidence = float(np.max(predictions[0])) * 100

                    css_class = CLASS_TO_CSS.get(predicted_class, "healthy")
                    icon = CLASS_ICONS.get(predicted_class, "🌱")
                    st.markdown(
                        f"<div class='prediction-badge {css_class}'>{icon} {predicted_class}</div>",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f"<div class='confidence'>Confidence: {confidence:.2f}%</div>",
                        unsafe_allow_html=True
                    )
                    st.progress(confidence / 100)
                except Exception as e:
                    st.error(f"Prediction failed: {str(e)}")
else:
    st.info("Please upload an image.")

st.markdown('<div class="footer-note">Potato Disease Classifier © 2025</div>', unsafe_allow_html=True)