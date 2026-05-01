import requests

API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

def get_ai_response(model_name, chat_history):
    # Penentuan Kepribadian Friendly
    if "Flash" in model_name:
        sys_p = "Anda GratacaUltraFlash 3.0WPPIDXM. Asisten yang super cepat, ramah, dan sangat membantu KAREEMXD."
    elif "Coding" in model_name:
        sys_p = "Anda GratacaUltraCoding 5.0WPPIDXM. Ahli teknologi yang sopan. Jawablah pertanyaan teknis KAREEMXD dengan sabar."
    else:
        sys_p = "Anda GratacaUltraZoom 4.0WPPIDXM. Analis strategi yang detail dan loyal. Bantu KAREEMXD dengan data yang akurat."

    payload = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": sys_p}] + chat_history
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    try:
        res = requests.post(URL, headers=headers, json=payload, timeout=20)
        return res.json()['choices'][0]['message']['content']
    except:
        return "Maaf Yang Mulia, otak saya sedikit tersendat. Coba ulangi pertanyaannya ya? 😊"
      
