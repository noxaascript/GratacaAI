import streamlit as st
from brain import get_ai_response

st.set_page_config(page_title="GratacaAI Supreme", page_icon="🚀", layout="wide")

# Header Minimalis
st.title("🚀 GratacaAI Supreme Ecosystem")
st.caption("Version 3.0WPPIDXM | Owner: KAREEMXD | Handphone Only")

# Sidebar untuk ganti Model
with st.sidebar:
    st.header("🤖 Model Selector")
    model_choice = st.selectbox(
        "Aktifkan Model:",
        ["GratacaUltraFlash 3.0WPPIDXM", "GratacaUltraCoding 5.0WPPIDXM", "GratacaUltraZoom 4.0WPPIDXM"]
    )
    st.divider()
    st.write(f"Status: **{model_choice} Aktif**")
    st.info("Karakter: **Friendly & Loyal**")
    if st.button("Reset Memory"):
        st.session_state.messages = []

# Chat System
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Apa yang bisa saya bantu hari ini, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_ai_response(model_choice, st.session_state.messages)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
