import json

# 读取 JSON 文件
with open('data/tree_structure.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# 存储SQL语句的列表
sql_statements = []

# 递归函数来遍历树结构并生成plat_path
def generate_plat_path(node, path=''):
    # 更新当前节点的path
    current_path = f"{path}-{node['BusinessTypeId']}" if path else f"{node['BusinessTypeId']}"
    
    # 生成SQL语句
    sql_statements.append(
        f"UPDATE process_plat SET plat_path = '{current_path}' WHERE id = {node['BusinessTypeId']};"
    )
    
    # 递归处理子节点
    for child in node.get('children', []):
        generate_plat_path(child, current_path)

# 遍历数据并生成SQL语句
for item in data:
    generate_plat_path(item)

# 保存SQL语句到文件
with open('data/oa/path.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_statements))


# 输出所有生成的SQL语句
for sql in sql_statements:
    print(sql)