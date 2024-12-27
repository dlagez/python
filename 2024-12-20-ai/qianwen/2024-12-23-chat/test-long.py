import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

file_object = client.files.create(file=Path("data/ai/发票-90123.2元.pdf"), purpose="file-extract")
print(file_object.id)
# test.pdf file-fe-DFOhTK7DfuzvAAcT5xITaNaY
# ht.pdf file-fe-Ho3laSfryxwyMyuYSduWiaoO
# 流程中台-软件定制开发合同.doc file-fe-XR8yF5tbyS6Uv668wIwrTpj1
# 发票-90123.2元.pdf file-fe-o8IlfDuwfx9CkSCsuepuV0g3