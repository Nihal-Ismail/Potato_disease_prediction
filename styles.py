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
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
                max-width: 800px;
                margin: auto;
                background: rgba(0,0,0,0.8);
                border-radius: 15px;
                padding: 2rem;
            }}

            /* Centered heading */
            .main-title {{
                text-align: center;
                font-size: 2rem;
                font-weight: 700;
                color: #FFC107;  /* Changed to warm yellow */
                text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
                margin-bottom: 1rem;
            }}

            hr {{
                border: 1px solid rgba(255,255,255,0.2);
                margin: 1rem 0;
            }}

            /* Image preview styling */
            .image-preview {{
                display: block;
                margin: 1rem auto;
                max-width: 250px;
                border-radius: 10px;
                border: 2px solid #FFD93D;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
            }}

            /* Prediction badge styling */
            .prediction-badge {{
                display: inline-block;
                padding: 10px 20px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 1.1rem;
                text-align: center;
                margin-top: 1rem;
            }}
            .early {{ background-color: #FF6B6B; color: white; }}
            .late {{ background-color: #6C63FF; color: white; }}
            .healthy {{ background-color: #4CAF50; color: white; }}

            /* Confidence text */
            .confidence {{
                font-size: 1rem;
                margin-top: 0.5rem;
                text-align: center;
                color: #8BC34A;  /* Changed to green-yellow */
                font-weight: bold;
            }}

            /* Footer note */
            .footer-note {{
                text-align: center;
                font-size: 0.8rem;
                color: rgba(255,255,255,0.6);
                margin-top: 1rem;
            }}
        </style>
    """, unsafe_allow_html=True)