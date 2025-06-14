import fitz  # PDF
from docx import Document  # Word

def extract_text(file, filetype):
    if filetype == "pdf":
        doc = fitz.open(stream=file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text

    elif filetype == "docx":
        document = Document(file)
        return "\n".join([para.text for para in document.paragraphs])

    else:
        return "🚫 Typ nicht unterstützt."  # نوع غير مدعوم
