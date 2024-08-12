import json

# 读取 JSON 文件
with open('data/aa_converted.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化字典，用于存储所有节点
id_to_node = {}

# 遍历数据列表，将所有节点放入字典中
for item in data['data']:
    # 添加一个 children 列表，用于存放子节点
    item['children'] = []
    id_to_node[item['BusinessTypeId']] = item

# 初始化一个列表，用于存储树的根节点
root_nodes = []

# 构建树结构
for item in data['data']:
    parent_id = item['ParentBusinessTypeId']
    if parent_id == 0:
        # 如果 ParentBusinessTypeId 为 0，则为根节点
        root_nodes.append(item)
    else:
        # 否则，将节点添加到其父节点的 children 列表中
        parent_node = id_to_node.get(parent_id)
        if parent_node:
            parent_node['children'].append(item)

# 将结果输出为树结构的 JSON 文件
with open('data/tree_structure.json', 'w', encoding='utf-8') as file:
    json.dump(root_nodes, file, ensure_ascii=False, indent=4)

# 如果你想查看树结构，可以直接打印
print(json.dumps(root_nodes, ensure_ascii=False, indent=4))
