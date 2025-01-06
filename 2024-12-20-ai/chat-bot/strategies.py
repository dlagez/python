from PyPDF2 import PdfReader
from docx import Document
import win32com.client

# 策略接口
class TextExtractionStrategy:
    def extract_text(self, file_path: str) -> str:
        pass

# 具体策略类：PDF提取
class PdfExtractionStrategy(TextExtractionStrategy):
    def extract_text(self, file_path: str) -> str:
        try:
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return None

# 具体策略类：Word提取
class WordExtractionStrategy(TextExtractionStrategy):
    def extract_text(self, file_path: str) -> str:
        try:
            doc = Document(file_path)
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        except Exception as e:
            print(f"Error reading Word file: {e}")
            return None

class WordExtractionStrategyDoc(TextExtractionStrategy):
    def extract_text(self, file_path: str) -> str:
        try:
            word = win32com.client.Dispatch("Word.Application")
            doc = word.Documents.Open(file_path)
            text = doc.Content.Text
            doc.Close()
            word.Quit()
            return text
        except Exception as e:
            print(f"Error reading Word file: {e}")
            return None

# 具体策略类：TXT提取
class TxtExtractionStrategy(TextExtractionStrategy):
    def extract_text(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return text
        except Exception as e:
            print(f"Error reading TXT file: {e}")
            return None
