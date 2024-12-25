import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

file_object = client.files.create(file=Path("data/ai/ht.pdf"), purpose="file-extract")
print(file_object.id)
# test.pdf file-fe-DFOhTK7DfuzvAAcT5xITaNaY
# ht.pdf file-fe-Ho3laSfryxwyMyuYSduWiaoO