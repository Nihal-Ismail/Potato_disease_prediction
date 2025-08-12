import base64
import streamlit as st

@st.cache_data
def get_bg_base64():
    with open("11.jpg", "rb") as bg_file:
        return base64.b64encode(bg_file.read()).decode()

def apply_styles(st):
    bg_base64 = get_bg_base64()

    st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

            html, body, [class*="stApp"] {{
                font-family: 'Poppins', sans-serif;
                background: url("data:image/jpeg;base64,{bg_base64}")
                            no-repeat center center fixed;
                background-size: cover;
                color: white;
            }}

            .block-container {{
                padding-top: 0.3rem !important;
                padding-bottom: 0.3rem !important;
                max-width: 650px;
                margin: auto;
                background: rgba(0,0,0,0.8);
                border-radius: 12px;
                padding: 1rem;
                max-height: 90vh;
                overflow-y: auto;
            }}

            .main-title {{
                text-align: center;
                font-size: 1.5rem;
                font-weight: 700;
                color: #FFC107;  
                text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
                margin-bottom: 0.5rem;
            }}

            hr {{
                border: 1px solid rgba(255,255,255,0.2);
                margin: 0.5rem 0;
            }}

            .image-preview {{
                display: block;
                margin: 0.5rem auto 0.3rem auto;
                max-width: 140px;
                border-radius: 8px;
                border: 2px solid #FFD93D;
                box-shadow: 0px 2px 10px rgba(0,0,0,0.5);
            }}

            .prediction-container {{
                text-align: center;
                margin-top: 0.4rem;
            }}

            .prediction-badge {{
                display: inline-block;
                padding: 6px 12px;
                border-radius: 15px;
                font-weight: bold;
                font-size: 0.9rem;
                text-align: center;
                margin-top: 0.3rem;
            }}
            .early {{ background-color: #FF6B6B; color: white; }}
            .late {{ background-color: #6C63FF; color: white; }}
            .healthy {{ background-color: #4CAF50; color: white; }}

            .confidence {{
                font-size: 0.85rem;
                margin-top: 0.2rem;
                text-align: center;
                color: #8BC34A;  
                font-weight: bold;
            }}

            .footer-note {{
                text-align: center;
                font-size: 0.7rem;
                color: rgba(255,255,255,0.6);
                margin-top: 0.5rem;
            }}
        </style>
    """, unsafe_allow_html=True)
