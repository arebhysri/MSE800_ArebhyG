import streamlit as st
from views import login

st.set_page_config(page_title="Car Rental System", page_icon="🚗")

st.title("Welcome to Car Rental System")

# Run login page
login.main()
