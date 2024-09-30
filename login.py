import streamlit as st
import database as db


def login():
    st.header("Login")
    username = st.text_input("Nutzername")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = db.get_user(username, password)
        if user:
            st.session_state.user = user
            st.success("Login erfolgreich!")
            st.rerun()  # Hier wurde die Änderung vorgenommen
        else:
            st.error("Fehlerhafter Nutzername oder falsches Passwort!")
