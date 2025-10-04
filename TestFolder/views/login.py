import streamlit as st

def main():
    st.subheader("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "1234":
            # Switch to adminDashboard page
            st.success("Login successful! Redirecting to Admin Dashboard...")
            st.switch_page("pages/adminDashboard.py")
        else:
            st.error("Invalid credentials")
