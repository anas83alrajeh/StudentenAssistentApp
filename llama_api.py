import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def query_llama(prompt):
    headers = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        # النموذج bart-large-cnn يرجع قائمة تحتوي على dict مع 'summary_text'
        if isinstance(result, list) and 'summary_text' in result[0]:
            return result[0]['summary_text']
        else:
            return "Antwort konnte nicht generiert werden."
    else:
        return f"Fehler von HuggingFace API: {response.status_code} {response.text}"
