import json

# 读取 JSON 文件
with open('data/aa.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 遍历 data 中的每个字典项，并将 BusinessTypeName 转换为中文
for item in data['data']:
    # 直接解码JSON数据中的转义字符
    item['BusinessTypeName'] = item['BusinessTypeName']

# 将转换后的数据写回文件或输出到控制台
with open('data/aa_converted.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 如果你想查看转换后的数据，可以直接打印
print(json.dumps(data, ensure_ascii=False, indent=4))
