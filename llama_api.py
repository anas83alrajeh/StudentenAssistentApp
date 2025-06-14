import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/your-model-name"  # استبدل your-model-name باسم النموذج الذي تستخدمه
HEADERS = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}

def query_llama(prompt: str) -> str:
    try:
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        # الرد حسب شكل البيانات:
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif isinstance(data, dict) and "error" in data:
            return f"Fehler von HuggingFace API: {data['error']}"
        else:
            # رد بديل إن لم يكن بالشكل المتوقع
            return str(data)
    except requests.exceptions.RequestException as e:
        return f"Fehler von HuggingFace API: {e}"
