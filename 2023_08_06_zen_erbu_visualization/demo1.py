import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


# 完整的数据量太大了，截取前100个数据作为测试样本
xlsx = ['data/di_row100_column2.xlsx', 
        'data/ding_row100_column2.xlsx', 
        'data/erbu_row100_column5.xlsx']

# 读取文件
erbu = pd.read_excel(xlsx[2], converters={'证券代码':str, 
                                             '人员ID':str, 
                                             '年份':str, 
                                             '权重':str})
di = pd.read_excel(xlsx[0], converters={'股票代码':str,
                                        '年份':str})
ding = pd.read_excel(xlsx[1], converters={'股票代码':str, 
                                            '年份':str})

# 读取erbu信息tolist
erbu_code = erbu['证券代码'].tolist()
erbu_id = erbu['人员ID'].tolist()
erbu_year = erbu['年份'].tolist()
erbu_weight = erbu['权重'].tolist()

# 读取di信息
di_code = di['股票代码'].tolist()
di_year = di['年份'].tolist()

# 读取ding信息
ding_code = ding['股票代码'].tolist()
ding_year = ding['年份'].tolist()


erbu = pd.read_excel(xlsx[2])
# read line from erbu with title:value
for index, row in erbu.iterrows():
    node_id = str(row['ID'])
    attributes = {key: str(value) for key, value in row.items() if key != 'ID'}  # 将数据转换为字符串
    G.add_node(node_id, **attributes)



# build a graph
G = nx.Graph()

G.add_nodes_from(erbu_code)
G.add_nodes_from(erbu_id)
G.add_nodes_from(erbu_year)
G.add_nodes_from(erbu_weight)



# 获取节点位置
pos = nx.spring_layout(G)
# 绘制节点
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
# 绘制边
nx.draw_networkx_edges(G, pos)
# 绘制节点标签
nx.draw_networkx_labels(G, pos, font_weight='bold')
plt.show()

