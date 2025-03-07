import streamlit as st
import pickle
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


background_image_url = "https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/SAKGwKC/medical-background-with-loop_n26ve-_yg_thumbnail-1080_05.png"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


VALID_USERS = {
    "admin": "password123",
    "doctor1": "docpass",
    "user1": "test123"
}

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None

def login():
    """Login function to authenticate users."""
    st.title("Login Page")

    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in VALID_USERS and VALID_USERS[username] == password:
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success(f"Welcome, {username}!")
            st.rerun()  # Refresh the page after login
        else:
            st.error("Invalid username or password!")

def main_page():
    """Main prediction page (after login)."""
    st.title("Lung Disease Prediction System")

    
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.rerun()

    
    try:
        model = pickle.load(open('Model/lungs_disease_model.sav', 'rb'))
    except FileNotFoundError:
        st.error("Model file not found! Ensure 'lungs_disease_model.sav' exists.")
        return

   
    st.write("Enter details for lung cancer prediction:")
    GENDER = st.number_input("Gender (1 = Male; 0 = Female)", step=1)
    AGE = st.number_input("Age", step=1)
    SMOKING = st.number_input("Smoking (1 = Yes; 0 = No)", step=1)
    YELLOW_FINGERS = st.number_input("Yellow Fingers (1 = Yes; 0 = No)", step=1)
    ANXIETY = st.number_input("Anxiety (1 = Yes; 0 = No)", step=1)
    PEER_PRESSURE = st.number_input("Peer Pressure (1 = Yes; 0 = No)", step=1)
    CHRONIC_DISEASE = st.number_input("Chronic Disease (1 = Yes; 0 = No)", step=1)
    FATIGUE = st.number_input("Fatigue (1 = Yes; 0 = No)", step=1)
    ALLERGY = st.number_input("Allergy (1 = Yes; 0 = No)", step=1)
    WHEEZING = st.number_input("Wheezing (1 = Yes; 0 = No)", step=1)
    ALCOHOL_CONSUMING = st.number_input("Alcohol Consuming (1 = Yes; 0 = No)", step=1)
    COUGHING = st.number_input("Coughing (1 = Yes; 0 = No)", step=1)
    SHORTNESS_OF_BREATH = st.number_input("Shortness Of Breath (1 = Yes; 0 = No)", step=1)
    SWALLOWING_DIFFICULTY = st.number_input("Swallowing Difficulty (1 = Yes; 0 = No)", step=1)
    CHEST_PAIN = st.number_input("Chest Pain (1 = Yes; 0 = No)", step=1)

    if st.button("Predict"):
        prediction = model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        result = "The person has lung cancer" if prediction[0] == 1 else "The person does not have lung cancer"
        st.success(result)



if st.session_state.authenticated:
    main_page()
else:
    login()
