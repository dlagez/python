from volcenginesdkarkruntime import Ark

# 豆包模型 Doubao-lite-4k
# Doubao-lite-4kDoubao-lite-4k|240328


client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)
# Image input:
response = client.chat.completions.create(
    model="ep-20241220102344-rcmq5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "这是哪里？"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://ark-project.tos-cn-beijing.ivolces.com/images/view.jpeg"
                    }
                },
            ],
        }
    ],
)

print(response.choices[0])