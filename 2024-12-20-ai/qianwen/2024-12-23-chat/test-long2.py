import os
from openai import OpenAI
import time

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
start_time = time.time()
completion = client.chat.completions.create(
    model="qwen-long",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        # {'role': 'system', 'content': 'fileid://file-fe-DFOhTK7DfuzvAAcT5xITaNaY'},
        {'role': 'system', 'content': f'fileid://file-fe-XR8yF5tbyS6Uv668wIwrTpj1,fileid://file-fe-o8IlfDuwfx9CkSCsuepuV0g3'},
        {'role': 'user', 'content': '我现在是审批人员,需要审批合同信息和发票金额是否一致，此发票为合同的第5支付节点，一年免费运维期满后支付的金额，发票为：file-fe-o8IlfDuwfx9CkSCsuepuV0g3，合同内容为file-fe-XR8yF5tbyS6Uv668wIwrTpj1，检查发票和合同的异常。'}
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

end_time = time.time()
response_time = end_time - start_time
print(f"Response Time: {response_time} seconds")