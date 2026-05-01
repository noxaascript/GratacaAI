import streamlit as st
import requests

API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

st.set_page_config(page_title="GratacaAI UltraFlash", page_icon="🚀")
st.title("🚀 GratacaAI UltraFlash 3.0WPPIDXM")
st.caption("Owner: KAREEMXD | Handphone Only")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("⚙️ System Control")
    mode = st.selectbox("Pilih Mode:", ["Normal", "Tech-Master", "Berserk"])
    if st.button("Hapus Chat"):
        st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Titah Anda, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if mode == "Normal": sys_p = "Anda GratacaAI, asisten pintar dan sopan untuk KAREEMXD."
    elif mode == "Tech-Master": sys_p = "Anda GratacaAI Tech-Master. Ahli SFS, coding, dan Android. Jawab teknis."
    else: sys_p = "Anda GratacaAI BERSERK. Kasar, toxic, tapi panggil KAREEMXD 'Yang Mulia'."

    payload = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": sys_p}] + st.session_state.messages
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    with st.chat_message("assistant"):
        try:
            res = requests.post(URL, headers=headers, json=payload)
            response = res.json()['choices'][0]['message']['content']
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            st.error("Koneksi Putus! 🖕")
          
