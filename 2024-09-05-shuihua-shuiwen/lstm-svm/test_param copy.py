import json

# 接收传递的 JSON 数据
json_data = '''
[{"id":39,"date":"2024-12-01","ammoniaNitrogen":1.932,"cod":23.718,"totalPhosphorus":0.167,"temperature":8.000,"humidity":32.000,"rainfall":0.000,"windSpeed":16.000,"sunshineDuration":10.320,"result":0},
{"id":38,"date":"2024-11-21","ammoniaNitrogen":0.539,"cod":35.404,"totalPhosphorus":0.200,"temperature":17.000,"humidity":64.000,"rainfall":0.000,"windSpeed":14.000,"sunshineDuration":10.480,"result":0}]
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 打印解析后的数据
print("Received JSON data:", data)

# 访问其中的某些字段
for item in data:
    print(f"ID: {item['id']}, Ammonia Nitrogen: {item['ammoniaNitrogen']}, COD: {item['cod']}, Temperature: {item['temperature']}")
