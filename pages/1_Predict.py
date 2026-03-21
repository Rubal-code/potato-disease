import streamlit as st
import requests
from PIL import Image
import io
from utils import apply_styles, sidebar

# Apply UI
apply_styles()
sidebar()

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

st.title("🔍 Predict Potato Disease")

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        with st.spinner("Analyzing..."):
            try:
                # Convert image to bytes
                img_bytes = io.BytesIO()
                image.save(img_bytes, format="JPEG")

                files = {"file": ("image.jpg", img_bytes.getvalue(), "image/jpeg")}
                
                # Send request to FastAPI
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    result = response.json()

                    # Raw prediction
                    predicted_class = result['class']
                    confidence = result['confidence']

                    # Mapping (MODEL → CLEAN NAME)
                    class_mapping = {
                        "Potato___Early_blight": "Early Blight",
                        "Potato___Late_blight": "Late Blight",
                        "Potato___healthy": "Healthy"
                    }

                    # Disease info
                    disease_info = {
                        "Early Blight": "🟤 Fungal disease causing brown spots with concentric rings. Usually starts on older leaves.",
                        "Late Blight": "⚠️ Severe disease causing dark lesions and rapid decay. Can destroy crops quickly.",
                        "Healthy": "✅ The leaf is healthy with no visible disease."
                    }

                    # Treatment suggestions
                    treatment = {
                        "Early Blight": "🌿 Use fungicides and remove infected leaves. Ensure proper spacing for airflow.",
                        "Late Blight": "🚨 Apply copper-based fungicide immediately. Remove affected plants to stop spread.",
                        "Healthy": "👍 No treatment needed. Maintain proper care."
                    }

                    # Convert class name
                    clean_name = class_mapping.get(predicted_class, predicted_class)

                    # Display results
                    st.success("Prediction Done ✅")

                    st.subheader("🧾 Result")
                    st.write(f"**Disease:** {clean_name}")
                    st.write(f"**Confidence:** {round(confidence * 100, 2)}%")

                    # Confidence bar
                    st.progress(float(confidence))

                    # Info
                    st.subheader("🦠 Disease Info")
                    st.info(disease_info.get(clean_name, "No info available"))

                    # Treatment
                    st.subheader("🌿 Recommended Action")
                    st.warning(treatment.get(clean_name, "No recommendation available"))

                else:
                    st.error("❌ API Error. Check backend.")

            except requests.exceptions.ConnectionError:
                st.error("🚨 Backend server is not running. Please start FastAPI.")

            except Exception as e:
                st.error(f"⚠️ Error: {e}")