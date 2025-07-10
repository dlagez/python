import requests

API_KEY = 'app-FuuYsnuon3Z1xCxP84qgqpOC'
CHAT_URL = 'https://dev-dify.hysz.co/v1/chat-messages'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

payload = {
    "inputs": {},
    "query": "你好?",
    "response_mode": "blocking",  # 或者 "streaming"
    "conversation_id": "",
    "user": "abc-123",
    "files": [
        {
            "type": "image",
            "transfer_method": "remote_url",
            "url": "https://cloud.dify.ai/logo/logo-site.png"
        }
    ]
}

response = requests.post(CHAT_URL, headers=headers, json=payload)
print(response.status_code)
print("返回内容：", response.text)  # 新增行
try:
    print("JSON解析：", response.json())
except Exception as e:
    print("❌ JSON解析失败：", e)
