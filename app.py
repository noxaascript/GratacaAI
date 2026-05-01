import streamlit as st
import requests

# --- SUPREME CONFIG ---
API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

st.set_page_config(page_title="GratacaAI Ecosystem", page_icon="🌐")

# --- UI STYLE (FIXED) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 GratacaAI Supreme Ecosystem")
st.caption("Owner: KAREEMXD | Handphone Only Edition")

# --- MODE SELECTOR ---
with st.sidebar:
    st.header("🚀 Pilih Model AI")
    model_choice = st.radio(
        "Aktifkan Model:",
        ["GratacaUltraFlash 3.0WPPIDXM", 
         "GratacaUltraCoding 5.0WPPIDXM", 
         "GratacaUltraZoom 4.0WPPIDXM"]
    )
    st.divider()
    if st.button("Reset Percakapan"):
        st.session_state.messages = []

# --- LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Apa yang bisa saya bantu, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Personality Logic
    if "Flash" in model_choice:
        sys_p = "Anda GratacaUltraFlash 3.0WPPIDXM. Cepat, ramah, dan friendly kepada KAREEMXD."
    elif "Coding" in model_choice:
        sys_p = "Anda GratacaUltraCoding 5.0WPPIDXM. Ahli coding dan teknologi, ramah kepada KAREEMXD."
    else:
        sys_p = "Anda GratacaUltraZoom 4.0WPPIDXM. Detail dalam analisis strategi game dan SFS, ramah kepada KAREEMXD."

    payload = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": sys_p}] + st.session_state.messages
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    with st.chat_message("assistant"):
        try:
            res = requests.post(URL, headers=headers, json=payload, timeout=30)
            response = res.json()['choices'][0]['message']['content']
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            st.error("Koneksi Putus! Coba lagi, Yang Mulia. 🖕")
            
