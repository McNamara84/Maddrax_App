import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import database as db
import login, register, members, chat, rewards, kasse, statistik

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None

# Set page config
st.set_page_config(
    page_title='MADDRAX Fanclub',
    page_icon=':book:',
    layout='wide'
)

# Sidebar navigation
def sidebar():
    with st.sidebar:
        if st.session_state.user:
            st.write(f"Logged in as: {st.session_state.user['username']}")
            st.write(f"Role: {st.session_state.user['role']}")
            st.write(f"Baxx: {st.session_state.user['baxx']}")
        
        choose = option_menu("MADDRAX Fanclub", 
                            ["Home", "Chat", "Rewards", "Kasse", "Statistik", "Members", "Logout"],
                            icons=['house', 'chat-dots', 'trophy', 'piggy-bank', 'graph-up', 'people', 'box-arrow-right'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
                                "container": {"padding": "5!important", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": "25px"}, 
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "#02ab21"},
                            }
                            )
        return choose

# Main app logic
def main():
    choice = sidebar()

    if not st.session_state.user:
        login.login()
        st.sidebar.button("Register", on_click=lambda: setattr(st.session_state, 'page', 'register'))
        if st.session_state.get('page') == 'register':
            register.register()
    else:
        if choice == "Home":
            st.title("Welcome to MADDRAX Fanclub")
            st.write("This is the official web app for MADDRAX Fanclub members.")
        elif choice == "Chat":
            chat.chat_page()
        elif choice == "Rewards":
            rewards.rewards_page()
        elif choice == "Kasse":
            kasse.kasse_page()
        elif choice == "Statistik":
            statistik.statistik_page()
        elif choice == "Members":
            members.members_page()
        elif choice == "Logout":
            st.session_state.user = None
            st.experimental_rerun()

if __name__ == "__main__":
    main()