import os
from strategies import PdfExtractionStrategy, WordExtractionStrategy, TxtExtractionStrategy

# 上下文类：文本提取器
class TextExtractor:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy

    def extract(self, file_path: str) -> str:
        return self.strategy.extract_text(file_path)

# 文件类型识别
def get_extraction_strategy(file_path: str):
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.pdf':
        return PdfExtractionStrategy()
    elif file_extension == '.docx':
        return WordExtractionStrategy()
    elif file_extension == '.txt':
        return TxtExtractionStrategy()
    else:
        print("Unsupported file format.")
        return None
