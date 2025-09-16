import streamlit as st
import random

def add_bg_from_url():
    st.markdown(
        """
        <style>

        .stApp {
            background-image: url("https://visme.co/blog/wp-content/uploads/2017/07/50-Beautiful-and-Minimalist-Presentation-Backgrounds-031.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }


        h1 {
            color: #ffffff;
            text-align: center;
        }


        label, .stNumberInput label, .stSelectbox label {
            color: #ffffff !important;
            font-weight: bold;
        }


        .stSuccess {
            background-color: rgba(255, 255, 255, 0.8);
            color: #000000;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


add_bg_from_url()

st.title("🎲 Number Guessing Game")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it?")

if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number_to_guess:
        st.warning("Too low! Try again. ⬆️")
    elif guess > st.session_state.number_to_guess:
        st.warning("Too high! Try again. ⬇️")
    else:
        st.success(
            f"🎉 Congratulations! You guessed the number {st.session_state.number_to_guess} correctly in {st.session_state.attempts} attempts!")
        st.balloons()

        # Reset the game
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0

if st.button("Start New Game"):
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.info("New game started! Guess a number between 1 and 100.")

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}     
    footer {visibility: hidden;}        
    header {visibility: hidden;}        
    </style>
    """,
    unsafe_allow_html=True
)
