def apply_styles(st):
    import base64

    # Read and encode the local background image
    with open("11.jpg", "rb") as bg_file:
        bg_base64 = base64.b64encode(bg_file.read()).decode()

    st.markdown(f"""
        <style>
            /* Import Google Font */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

            html, body, [class*="stApp"] {{
                font-family: 'Poppins', sans-serif;
                background: url("data:image/jpeg;base64,{bg_base64}")
                            no-repeat center center fixed;
                background-size: cover;
                color: white;
            }}

            /* Main container styling */
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

            /* Centered heading */
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

            /* Image preview styling */
            .image-preview {{
                display: block;
                margin: 0.5rem auto 0.3rem auto;
                max-width: 140px;  /* smaller image */
                border-radius: 8px;
                border: 2px solid #FFD93D;
                box-shadow: 0px 2px 10px rgba(0,0,0,0.5);
            }}

            /* Prediction container */
            .prediction-container {{
                text-align: center;
                margin-top: 0.4rem;
            }}

            /* Prediction badge styling */
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

            /* Confidence text */
            .confidence {{
                font-size: 0.85rem;
                margin-top: 0.2rem;
                text-align: center;
                color: #8BC34A;  
                font-weight: bold;
            }}

            /* Footer note */
            .footer-note {{
                text-align: center;
                font-size: 0.7rem;
                color: rgba(255,255,255,0.6);
                margin-top: 0.5rem;
            }}
        </style>
    """, unsafe_allow_html=True)
