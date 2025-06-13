import streamlit as st
from file_processing import extract_text, split_text_to_paragraphs
from similarity_search import find_most_similar_paragraph
from llama_api import query_llama
from chat_storage import save_conversation, load_conversation

st.set_page_config(page_title="Studenten- und Forschungsassistent", layout="wide")
st.title("Studenten- und Forschungsassistent mit LLaMA")

uploaded_file = st.file_uploader("Datei hochladen (PDF, Word oder Bild)", type=["pdf", "docx", "jpg", "jpeg", "png"])

if uploaded_file:
    file_type = uploaded_file.type.split('/')[-1]
    if "word" in uploaded_file.type:
        file_type = "docx"
    elif "pdf" in uploaded_file.type:
        file_type = "pdf"
    elif "image" in uploaded_file.type:
        file_type = uploaded_file.type.split('/')[-1]
    else:
        st.error("Dateiformat wird nicht unterstützt.")

    raw_text = extract_text(uploaded_file, file_type)
    paragraphs = split_text_to_paragraphs(raw_text)

    chat_history = load_conversation()
    user_question = st.text_input("Ihre Frage hier eingeben")

    if user_question:
        context = find_most_similar_paragraph(user_question, paragraphs)
        prompt = f"""Beantworte die folgende Frage basierend ausschließlich auf dem unten stehenden Text:

Text:
"""{context}"""

Frage: {user_question}
Antwort:"""

        bot_response = query_llama(prompt)

        st.markdown(f"**Sie:** {user_question}")
        st.markdown(f"**Bot:** {bot_response}")

        save_conversation(user_question, bot_response)

    if chat_history:
        st.markdown("---")
        st.subheader("Vorherige Gespräche")
        for chat in chat_history:
            st.markdown(f"**Sie:** {chat['user']}")
            st.markdown(f"**Bot:** {chat['bot']}")
else:
    st.info("Bitte laden Sie eine Datei hoch, um zu starten")

st.markdown("---")
st.markdown("""
<p style="text-align:center; font-size:12px; color:gray;">
    Kontakt:<br>
    Erstellt von Anas Al Rajeh<br>
    Email: <a href="mailto:anasalrajeh9@gmail.com">anasalrajeh9@gmail.com</a>
</p>
""", unsafe_allow_html=True)