import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-long",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        # {'role': 'system', 'content': 'fileid://file-fe-DFOhTK7DfuzvAAcT5xITaNaY'},
        {'role': 'system', 'content': 'fileid://file-fe-Ho3laSfryxwyMyuYSduWiaoO'},
        {'role': 'user', 'content': '我现在是审批人员，需要审批表单信息和合同内容是否匹配，表单数据：合同金额90万，合同内容为pdf file-fe-Ho3laSfryxwyMyuYSduWiaoO'}
    ],
    stream=True,
    stream_options={"include_usage": True}
)

full_content = ""
for chunk in completion:
    if chunk.choices and chunk.choices[0].delta.content:
        full_content += chunk.choices[0].delta.content
        print(chunk.model_dump())

print({full_content})