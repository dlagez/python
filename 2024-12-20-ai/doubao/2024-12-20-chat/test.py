from volcenginesdkarkruntime import Ark

# 豆包模型 Doubao-lite-4k
# Doubao-lite-4kDoubao-lite-4k|240328
client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="ep-20241220093718-lsmht",
    messages = [
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "武汉的房价最近怎么样，大概范围是多少？"},
    ],
)
print(completion.choices[0].message.content)

# # Streaming:
# print("----- streaming request -----")
# stream = client.chat.completions.create(
#     model="ep-20241220093718-lsmht",
#     messages = [
#         {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
#         {"role": "user", "content": "常见的十字花科植物有哪些？"},
#     ],
#     stream=True
# )
# for chunk in stream:
#     if not chunk.choices:
#         continue
#     print(chunk.choices[0].delta.content, end="")
# print()