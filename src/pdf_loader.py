import os
import PyPDF2

class PDFLoader:
    """Loads and extracts text from PDF files in the WA_PDF directory."""

    def __init__(self, folder="WA_PDF"):
        self.folder = folder

    def load_pdfs(self):
        """Loads all PDFs from the folder and extracts text."""
        pdf_texts = []
        for filename in os.listdir(self.folder):
            if filename.endswith(".pdf"):
                file_path = os.path.join(self.folder, filename)
                text = self.extract_text_from_pdf(file_path)
                pdf_texts.append({"filename": filename, "text": text})
        return pdf_texts

    def extract_text_from_pdf(self, filepath):
        """Extracts text from a single PDF file."""
        with open(filepath, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text
