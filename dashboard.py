import streamlit as st
import database as db

def show_dashboard():
    st.title("Dashboard")
    
    # Begrüßung
    st.header("Herzlich willkommen im weltweit größten Maddrax-Vereinsheim!")
    
    # Benutzerinformationen
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Baxx", st.session_state.user['baxx'])
    with col2:
        st.metric("Rolle", st.session_state.user['role'])
    
    # Aktuelle News
    st.subheader("Ankündigungen")
    news = db.get_latest_news()
    if news:
        with st.expander(news['title'], expanded=True):
            st.write(news['content'])
            st.caption(f"Veröffentlicht am: {news['date']}")
    else:
        st.info("Keine aktuellen Ankündigungen vorhanden.")
    
    # Platzhalter für zukünftige Dashboard-Elemente
    st.subheader("Aktivitäten")
    st.info("Hier können zukünftig Aktivitäten oder Statistiken angezeigt werden.")