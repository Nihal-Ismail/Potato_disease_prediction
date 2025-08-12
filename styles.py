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
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            html, body, [class*="css"] {{
                font-family: 'Poppins', sans-serif;
            }}
            .stApp {{
                background: url(data:image/jpg;base64,{bg_base64}) no-repeat center center fixed;
                background-size: cover;
            }}
            h1 {{
                color: #ffffff;
                text-align: center;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            }}
            .stSuccess {{
                font-size: 20px;
                font-weight: 600;
                color: #ffffff;
                background-color: rgba(0, 128, 0, 0.7);
                padding: 12px;
                border-radius: 10px;
                text-align: center;
            }}
        </style>
    """, unsafe_allow_html=True)
