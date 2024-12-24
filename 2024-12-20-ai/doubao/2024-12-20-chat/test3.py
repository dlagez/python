from volcenginesdkarkruntime import Ark

# 豆包模型 智能体测试，支持文档解析


client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)
# Image input:
response = client.bot_chat.completions.create(
    model="bot-20241220104949-jbvh9",
    messages=[
            {
        "content": "总结文档",
        }
    ],
)

print(response.choices[0].message.content)
print(response.references)