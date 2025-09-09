import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="TheraBot", page_icon="🌿")
st.title("🌿 TheraBot - Empathetic AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("How are you feeling today?")

if user_input:
    payload = {"query": user_input, "session_id": "web"}
    res = requests.post(API_URL, json=payload).json()
    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", res["response"]))

    if res["crisis_detected"]:
        st.warning(res["helpline"])

for role, msg in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
