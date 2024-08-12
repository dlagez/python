import json

# 读取 JSON 文件
with open('data/oa/15.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# 递归函数生成SQL插入语句
def generate_sql(data, sql_statements):
    try:
        order_num = int(data['OrderNumber'])
    except ValueError:
        order_num = 1
    sql = f"""
    INSERT INTO process_plat (id, parent_id, plat_name, plat_code, order_num, org_id)
    VALUES ({data['BusinessTypeId']}, {data['ParentBusinessTypeId']}, '{data['BusinessTypeName']}', '{data['BusinessTypeCode']}', {order_num}, 6320);
    """
    sql_statements.append(sql)

    # 递归处理子节点
    if 'children' in data:
        for child in data['children']:
            generate_sql(child, sql_statements)

# 初始化SQL语句列表
sql_statements = []
generate_sql(data, sql_statements)

# 保存SQL语句到文件
with open('data/oa/15.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_statements))

print("SQL语句已生成并保存到文件 insert_statements.sql 中")