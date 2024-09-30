import streamlit as st
import database as db


def register():
    st.header("Registrierung")
    new_username = st.text_input("Wähle einen Nutzernamen")
    new_password = st.text_input("Wähle ein Passwort", type="password")
    confirm_password = st.text_input("Passwort bestätigen", type="password")

    if st.button("Registrierung", key="register_button"):
        if not new_username:
            st.error("Bitte Nutzernamen eingeben")
        elif db.user_exists(new_username):
            st.error("Dieser Nutzername ist bereits vergeben. Bitte wähle einen anderen.")
        elif new_password != confirm_password:
            st.error("Passwort stimmt nicht überein")
        elif len(new_password) < 6:
            st.error("Passwort muss min. 6 Zeichen lang sein")
        else:
            try:
                db.add_user(new_username, new_password)
                st.success("Registrierung erfolgreich. Du kannst dich jetzt anmelden.")
                st.session_state.page = 'login'
            except Exception as e:
                st.error(f"Registrierung fehlgeschlagen: {str(e)}")
