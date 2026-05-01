import requests
from identity import MODELS

API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

def get_ai_response(model_name, chat_history):
    # Mengambil identitas dari file identity.py
    sys_p = MODELS.get(model_name, {}).get("prompt", "Anda adalah asisten ramah.")

    payload = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": sys_p}] + chat_history,
        "temperature": 0.7
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/noxaascript/GratacaAI"
    }

    try:
        res = requests.post(URL, headers=headers, json=payload, timeout=20)
        res.raise_for_status() # Cek jika ada error koneksi
        data = res.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"Waduh Yang Mulia, ada gangguan teknis sedikit: {str(e)}. Coba sapa lagi ya? 😊"
        
