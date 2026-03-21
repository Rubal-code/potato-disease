import streamlit as st
from utils import apply_styles, sidebar

apply_styles()
sidebar()

st.title("📖 About Project")

st.markdown("""
## 🥔 Potato Disease Detection System

This is an **AI-powered web application** that detects potato plant diseases from leaf images using Deep Learning.

The goal is to help farmers and agricultural systems identify diseases early and take preventive actions 🌱

---

## 🌱 Problem Statement

Potato plants are affected by diseases like:
- Early Blight  
- Late Blight  

Manual detection is:
- ❌ Time-consuming  
- ❌ Requires expertise  
- ❌ Not scalable  

👉 This system automates the process using AI.

---

## 🧠 Model Details

- Built using **CNN (Convolutional Neural Networks)**
- Trained on potato leaf dataset
- Classifies images into:
  - Healthy
  - Early Blight
  - Late Blight

---

## ⚙️ How It Works

1. Upload image via Streamlit UI  
2. Image sent to FastAPI backend  
3. Model processes image  
4. Prediction returned with confidence  

---

## 🚀 Tech Stack

- **Frontend:** Streamlit (Multi-page UI)  
- **Backend:** FastAPI  
- **ML:** TensorFlow / Keras  
- **Image Processing:** PIL, NumPy  

---

## 📊 Features

- 📤 Image Upload  
- 🔍 Real-time Prediction  
- 📈 Confidence Score  
- 🌙 Dark Mode UI  
- 📄 Multi-page Navigation  

---

## 👨‍💻 Developer

**Rubal Singh** 🚀  

- 💻 Full Stack Java Developer  
- 🤖 AI/ML Enthusiast  
- 📊 Data Science Learner  

---

## 🔗 Connect With Me

- 💻 GitHub: https://github.com/Rubal-code  
- 💼 LinkedIn: https://www.linkedin.com/in/rubal-kundra/  
- 🌐 Portfolio: https://data-curious-creator.lovable.app/  

---

## 🎯 Future Improvements

- 📊 Prediction history dashboard  
- ☁️ Cloud deployment  
- 📱 Mobile-friendly UI  
- 🎤 Voice-based input  

---

## 📌 Conclusion

This project shows how **AI + Web Development** can solve real-world agricultural problems 🌾

👉 Moving towards **smart farming**
""")