import fitz  # PDF
from docx import Document  # Word
from PIL import Image  # Bilder
import pytesseract  # OCR

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

    elif filetype in ["jpg", "jpeg", "png"]:
        image = Image.open(file)
        return pytesseract.image_to_string(image)

    else:
        return "🚫 Typ nicht unterstützt."

def split_text_to_paragraphs(text, min_length=50):
    raw_paragraphs = text.split('\n')
    paragraphs = []
    temp = ""
    for line in raw_paragraphs:
        if line.strip() == "":
            if len(temp) >= min_length:
                paragraphs.append(temp.strip())
            temp = ""
        else:
            temp += " " + line.strip()
    if len(temp) >= min_length:
        paragraphs.append(temp.strip())
    return paragraphs