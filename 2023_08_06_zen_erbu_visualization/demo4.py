import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 读取Excel文件
# di = pd.read_excel('data/di_row100_column2.xlsx')
# ding = pd.read_excel('data/ding_row100_column2.xlsx')
# erbu = pd.read_excel('data/erbu_row100_column5.xlsx')


# di = pd.read_excel('data/di.xlsx', dtype=str)
# ding = pd.read_excel('data/ding.xlsx', dtype=str)
# erbu = pd.read_excel('data/erbu.xlsx', dtype=str)

# dif = di[di['年份'] == '2011']
# dingf = ding[ding['年份'] == '2011']
# erbuf = erbu[erbu['年份'] == '2011']
# dif.to_excel('data/di_2011.xlsx')
# dingf.to_excel('data/ding_2011.xlsx')
# erbuf.to_excel('data/erbu_2011.xlsx')

xlsx_names = ['data/di_2009.xlsx', 'data/ding_2009.xlsx', 'data/erbu_2009.xlsx']
# xlsx_names = ['data/di_2010.xlsx', 'data/ding_2010.xlsx', 'data/erbu_2010.xlsx']
# xlsx_names = ['data/di_2011.xlsx', 'data/ding_2011.xlsx', 'data/erbu_2011.xlsx']
di = pd.read_excel(xlsx_names[0], dtype=str)
ding = pd.read_excel(xlsx_names[1], dtype=str)
erbu = pd.read_excel(xlsx_names[2], dtype=str)


# 创建一个无向图
G = nx.Graph()

# 将每一行的数据转换为字符串，并将其作为节点添加到图中
for index, row in di.iterrows():
    # 人员ID作为节点的唯一标识符来存储人的信息
    person_id = row['人员ID']
    # 将所有数据作为节点的属性
    attributes = {key: str(value) for key, value in row.items()}  # 将数据转换为字符串
    G.add_node(person_id, **attributes)

for index, row in di.iterrows():
    # 股票代码 作为节点的唯一标识符来存储公司信息
    code = row['股票代码']
    # 将所有数据作为节点的属性
    attributes = {key: str(value) for key, value in row.items()}  # 将数据转换为字符串
    G.add_node(code, **attributes)

# 添加边
for index, row in erbu.iterrows():
    stock_code = row['证券代码']
    person_id = row['人员ID']
    G.add_edge(stock_code, person_id)  # 使用解包操作将元组拆分成两个节点标识符



# 绘制图形
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()


print(G.nodes)
print(G.nodes[(1, 3027280)])
print(G)