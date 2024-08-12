import json

# 读取 JSON 文件
with open('data/jituan.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# 递归生成 plat_path 并生成 SQL 语句
def generate_plat_path(data, parent_path, sql_statements):
    current_path = f"{parent_path}/{data['BusinessTypeId']}" if parent_path else f"/{data['BusinessTypeId']}"
    
    sql = f"""
    UPDATE process_plat
    SET plat_path = '{current_path}'
    WHERE id = {data['BusinessTypeId']};
    """
    sql_statements.append(sql)
    
    # 递归处理子节点
    if 'children' in data:
        for child in data['children']:
            generate_plat_path(child, current_path, sql_statements)

# 初始化 SQL 语句列表
sql_statements = []

# 处理每一个第一层的对象
for company in data:
    generate_plat_path(company, "", sql_statements)

# 保存 SQL 语句到文件
with open('update_plat_path.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_statements))

print("SQL语句已生成并保存到文件 update_plat_path.sql 中")