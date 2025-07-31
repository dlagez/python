import os
from docx import Document
import win32com.client
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False
)

def extract_docx_text(filepath):
    doc = Document(filepath)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_doc_text(filepath):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(filepath)
    text = doc.Content.Text
    doc.Close(False)
    word.Quit()
    return text

def extract_word_text(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".docx":
        return extract_docx_text(filepath)
    elif ext == ".doc":
        return extract_doc_text(filepath)
    else:
        raise ValueError(f"不支持的文件格式: {ext}")

def extract_pdf_text(filepath):
    try:
        result = ocr.predict(filepath)
        texts = []
        for res in result:
            json_data = res.json.get('res', {})
            texts.extend(json_data.get("rec_texts", []))
        return "\n".join(texts)
    except Exception as e:
        print(f"提取 PDF 错误：{filepath}，错误：{e}")
        return None

def save_text_to_txt(filepath, text):
    txt_path = os.path.splitext(filepath)[0] + ".txt"
    if os.path.exists(txt_path):
        print(f"已存在，跳过：{txt_path}")
        return
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"已保存：{txt_path}")

def process_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext in [".doc", ".docx"]:
        try:
            text = extract_word_text(filepath)
            if text:
                save_text_to_txt(filepath, text)
        except Exception as e:
            print(f"Word 处理失败：{filepath}，错误：{e}")
    elif ext == ".pdf":
        try:
            text = extract_pdf_text(filepath)
            if text:
                save_text_to_txt(filepath, text)
        except Exception as e:
            print(f"PDF 处理失败：{filepath}，错误：{e}")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith((".pdf", ".docx", ".doc")):
                filepath = os.path.join(root, filename)
                process_file(filepath)

if __name__ == "__main__":
    base_dir = r"D:\Download\all07163"
    for project_name in os.listdir(base_dir):
        project_path = os.path.join(base_dir, project_name)
        if os.path.isdir(project_path):
            for subfolder in ["合同创建附件列表", "合同最终附件列表"]:
                subfolder_path = os.path.join(project_path, subfolder)
                if os.path.exists(subfolder_path):
                    print(f"\n开始处理：{subfolder_path}")
                    process_folder(subfolder_path)
