import streamlit as st
import database as db


def login():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = db.get_user(username, password)
        if user:
            st.session_state.user = user
            st.success("Logged in successfully!")
            st.rerun()  # Hier wurde die Änderung vorgenommen
        else:
            st.error("Invalid username or password")
