import streamlit as st
import requests

API_URL = "https://fitness-coach-agent.onrender.com/chat"

st.title("AI Fitness Coach")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your fitness coach")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Show loading spinner
    with st.spinner("Generating response..."):

        response = requests.post(
            API_URL,
            json={
                "user_id": "web_user",
                "message": user_input
            }
        )

        reply = response.json()["reply"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    with st.chat_message("assistant"):
        st.markdown(reply)