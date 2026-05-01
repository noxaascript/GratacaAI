import streamlit as st
import requests

# --- SUPREME CONFIG ---
API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

st.set_page_config(page_title="GratacaAI Ecosystem", page_icon="🌐", layout="centered")

# --- UI STYLE ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(45deg, #00f2fe, #4facfe); color: white; border: none; }
    </style>
    """, unsafe_allow_stdio=True)

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
    st.success(f"{model_choice} Aktif!")
    if st.button("Clear Memory"):
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
        sys_p = "Anda GratacaUltraFlash 3.0WPPIDXM. Sangat cepat, ramah, dan membantu KAREEMXD dalam segala hal umum."
    elif "Coding" in model_choice:
        sys_p = "Anda GratacaUltraCoding 5.0WPPIDXM. Jenius coding, Python, Termux, dan hardware Android. Jawab secara teknis tapi tetap friendly kepada KAREEMXD."
    else:
        sys_p = "Anda GratacaUltraZoom 4.0WPPIDXM. Fokus pada analisis mendalam, strategi game (FC Mobile/FF), dan Spaceflight Simulator. Sangat detail dan loyal pada KAREEMXD."

    payload = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": sys_p}] + st.session_state.messages
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    with st.chat_message("assistant"):
        try:
            res = requests.post(URL, headers=headers, json=payload, timeout=30)
            res_json = res.json()
            if 'choices' in res_json:
                response = res_json['choices'][0]['message']['content']
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.error("API Limit atau Eror! Coba lagi sebentar, Yang Mulia. 🖕")
        except:
            st.error("Koneksi Putus! Pastikan Sinyal Pekanbaru Stabil. 🖕")
            
