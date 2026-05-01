import streamlit as st
import time

def show_loading():
    with st.spinner("Menghubungkan ke satelit UltraFlash..."):
        time.sleep(0.5)

def greet_owner(name):
    st.toast(f"Selamat datang kembali, Yang Mulia {name}! 👑")
  
