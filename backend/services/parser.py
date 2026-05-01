import fitz  # PyMuPDF

def extract_text(file_bytes):
    with open("temp.pdf", "wb") as f:
        f.write(file_bytes)

    doc = fitz.open("temp.pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text.lower()
