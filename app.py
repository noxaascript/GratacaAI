import streamlit as st
from brain import get_ai_response
from style import apply_custom_style
from utils import greet_owner, show_loading
from config import APP_NAME, VERSION, OWNER_NAME

st.set_page_config(page_title=APP_NAME, page_icon="🚀")
apply_custom_style()

if "greeted" not in st.session_state:
    greet_owner(OWNER_NAME)
    st.session_state.greeted = True

st.title(f"🚀 {APP_NAME}")
st.caption(f"Version {VERSION} | Owner: {OWNER_NAME} | Handphone Only")

with st.sidebar:
    st.header("🤖 Model Selector")
    model_choice = st.selectbox("Aktifkan Model:", ["GratacaUltraFlash 3.0WPPIDXM", "GratacaUltraCoding 5.0WPPIDXM", "GratacaUltraZoom 4.0WPPIDXM"])
    st.divider()
    if st.button("Reset Memory"):
        st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Apa titah Anda, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        show_loading()
        response = get_ai_response(model_choice, st.session_state.messages)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
