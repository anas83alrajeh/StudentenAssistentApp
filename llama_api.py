import requests

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"

def query_llama(question, context):
    import streamlit as st  # استيراد streamlit داخل الدالة

    HEADERS = {
        "Authorization": f"Bearer {st.secrets['HF_API_KEY']}"
    }

    try:
        payload = {
            "inputs": {
                "question": question,
                "context": context
            }
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=20)
        if response.status_code == 200:
            return response.json().get("answer", "Keine Antwort gefunden.")
        else:
            return f"Fehler von HuggingFace API: {response.status_code}"
    except Exception as e:
        return f"Fehler beim API-Aufruf: {e}"
