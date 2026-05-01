import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; }
        .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
        .stChatInputContainer { padding-bottom: 20px; }
        st-emotion-cache-16idsys p { font-size: 1.1rem; }
        </style>
    """, unsafe_allow_html=True)
  
