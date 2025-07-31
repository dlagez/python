import os
from docx import Document
import win32com.client

def extract_docx_text(filepath):
    """提取 docx 文件的文本内容"""
    doc = Document(filepath)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_doc_text(filepath):
    """提取 doc 文件的文本内容"""
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(filepath)
    text = doc.Content.Text
    doc.Close(False)
    word.Quit()
    return text

def extract_word_text(filepath):
    """根据后缀选择不同提取方式"""
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".docx":
        return extract_docx_text(filepath)
    elif ext == ".doc":
        return extract_doc_text(filepath)
    else:
        raise ValueError(f"不支持的文件格式: {ext}")

def save_text_to_txt(filepath, text):
    """将文本内容保存为同名 .txt 文件"""
    txt_path = os.path.splitext(filepath)[0] + ".txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"已保存：{txt_path}")

def process_folder(folder_path):
    """批量处理文件夹内的 Word 文件"""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".docx", ".doc")):
            filepath = os.path.join(folder_path, filename)
            try:
                text = extract_word_text(filepath)
                save_text_to_txt(filepath, text)
            except Exception as e:
                print(f"处理失败：{filename}，错误：{e}")

# 示例用法
if __name__ == "__main__":
    folder_path = r"D:\Download\all07162\(父)济南遥墙机场配套设施项目C6-05地块3#旅客过夜用房精装修施工总承包\合同创建附件列表"  # 修改为你的文件夹路径
    process_folder(folder_path)

