import os
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import time
import base64
from io import BytesIO
from styles import apply_styles

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

# --------- Load TensorFlow SavedModel ---------
@st.cache_resource
def load_model():
    """Load TF SavedModel and return the serving function."""
    model_path = os.path.join(os.path.dirname(__file__), "saved_models", "1")
    loaded = tf.saved_model.load(model_path)
    infer = loaded.signatures["serving_default"]
    return infer

# --------- Utilities ---------
def image_to_base64(img_array):
    """Convert numpy image array to base64 string for HTML display."""
    img = Image.fromarray(img_array.astype('uint8'))
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def read_image(image_file):
    """Read and convert uploaded image to numpy array."""
    try:
        image = Image.open(image_file).convert("RGB")
        return np.array(image)
    except Exception as e:
        st.error(f"Image loading failed: {str(e)}")
        return None

# --------- Main App ---------
if __name__ == "__main__":
    # Page settings
    st.set_page_config(
        page_title="Potato Disease Classifier",
        page_icon="🥔",
        layout="centered"
    )

    # Apply custom CSS/background
    apply_styles(st)

    # Load model
    MODEL = load_model()

    # Title & instructions
    st.markdown('<div class="main-title">🥔 Potato Disease Classifier</div>', unsafe_allow_html=True)
    st.markdown('<hr />', unsafe_allow_html=True)

    # File uploader with accessible label
    uploaded_file = st.file_uploader(
        "Upload a potato leaf image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        image_np = read_image(uploaded_file)

        if image_np is not None:
            # Show preview
            img_b64 = image_to_base64(image_np)
            st.markdown(
                f"<img src='data:image/png;base64,{img_b64}' class='image-preview'/>",
                unsafe_allow_html=True
            )

            with st.spinner("Analyzing ..."):
                time.sleep(1.2)  # Simulate short processing delay

                # Preprocess for model
                img_batch = np.expand_dims(image_np, 0)
                img_batch = tf.convert_to_tensor(img_batch, dtype=tf.float32)

                try:
                    # Call the saved model function
                    outputs = MODEL(img_batch)

                    # Extract predictions from dict
                    predictions = list(outputs.values())[0].numpy()

                    # Get predicted class and confidence
                    class_idx = int(np.argmax(predictions[0]))
                    predicted_class = CLASS_NAMES[class_idx]
                    confidence = float(np.max(predictions[0])) * 100

                    # Visuals
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

    # Footer
    st.markdown('<div class="footer-note">Potato Disease Classifier © 2025</div>', unsafe_allow_html=True)
