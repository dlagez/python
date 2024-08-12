import json

# 读取 JSON 文件
with open('data/oa/02-yigs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

company_map = {
    "集团总部": 6319,
    "致远建设": 6325,
    "天创建设": 6326,
    "博宏建设": 6322,
    "钟鑫建设": 6337,
    "五公司": 6328,
    "六公司": 6324,
    "致远建设": 6325,
    "致远建设": 6325,
    "致远建设": 6325,
    
}

# 递归函数生成SQL插入语句
def generate_sql(data, sql_statements, org_id):
    try:
        order_num = int(data['OrderNumber'])
    except ValueError:
        order_num = 1
    if (org_id is None):
        org_id = company_map.get(data['BusinessTypeName'], 0)
    


    sql = f"""
    INSERT INTO process_plat (id, parent_id, plat_name, plat_code, order_num, org_id)
    VALUES ({data['BusinessTypeId']}, {data['ParentBusinessTypeId']}, '{data['BusinessTypeName']}', '{data['BusinessTypeCode']}', {order_num}, org_id);
    """
    sql_statements.append(sql)

    # 递归处理子节点
    if 'children' in data:
        for child in data['children']:
            generate_sql(child, sql_statements)

# 初始化SQL语句列表
sql_statements = []
generate_sql(data, sql_statements,None)

# 保存SQL语句到文件
with open('data/oa/02-yigs.sql', 'w', encoding='utf-8') as file:
    file.write("\n".join(sql_statements))

print("SQL语句已生成并保存到文件 insert_statements.sql 中")