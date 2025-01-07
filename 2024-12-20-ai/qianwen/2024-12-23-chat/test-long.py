import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

file_object = client.files.create(file=Path(r"D:\Document\WXWork\1688855251474475\Cache\Image\2025-01\企业微信截图_1736155475416.png"), purpose="file-extract")
print(file_object.id)
# test.pdf file-fe-DFOhTK7DfuzvAAcT5xITaNaY
# ht.pdf file-fe-Ho3laSfryxwyMyuYSduWiaoO
# 流程中台-软件定制开发合同.doc file-fe-XR8yF5tbyS6Uv668wIwrTpj1
# 发票-90123.2元.pdf file-fe-o8IlfDuwfx9CkSCsuepuV0g3
# 企微发票截图 file-fe-91ERzUJNxmXugxQ5OnOgbFIV
# 企微发票截图 file-fe-l9e6dOOb04bGHYb36bnqhuN0