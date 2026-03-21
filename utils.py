import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* App background */
        .stApp {
            background-color: #0e1117;
        }

        /* Main text */
        .stApp, .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #161a23;
        }

        /* Sidebar text */
        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Buttons */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }

        /* File uploader */
        .stFileUploader {
            border: 2px dashed #4CAF50;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
    """, unsafe_allow_html=True)


def sidebar():
    st.sidebar.title("🥔 Potato AI")
    st.sidebar.info("Navigate using pages above 👆")