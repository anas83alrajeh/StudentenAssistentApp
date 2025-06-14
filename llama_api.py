import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/mbien/mt5-small-german-question-answering"
headers = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}

def query_llama(prompt):
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        # بناء على شكل الرد من Hugging Face
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        else:
            return "Antwort konnte nicht generiert werden."
    except requests.exceptions.HTTPError as e:
        return f"Fehler von HuggingFace API: {e.response.status_code} {e.response.reason}"
    except Exception as e:
        return f"Allgemeiner Fehler: {e}"
