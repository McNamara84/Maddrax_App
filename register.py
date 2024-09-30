import streamlit as st
import database as db


def register():
    st.header("Register")
    new_username = st.text_input("Choose a username")
    new_password = st.text_input("Choose a password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    if st.button("Register", key="register_button"):  # Added a unique key here
        if new_password != confirm_password:
            st.error("Passwords do not match")
        elif len(new_password) < 6:
            st.error("Password must be at least 6 characters long")
        else:
            try:
                db.add_user(new_username, new_password)
                st.success("Registration successful! You can now log in.")
                st.session_state.page = 'login'
            except Exception as e:
                st.error(f"Registration failed: {str(e)}")
