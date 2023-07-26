import pandas as pd
import networkx as nx

# 读取Excel文件
df = pd.read_excel('tu.xlsx', sheet_name='Sheet1')

# 创建一个空的二部图加时空图
B = nx.Graph()

# 获取顶部节点列表和底部节点列表
top_nodes = list(set(df['证券代码'].tolist()))
bottom_nodes = list(set(df['人员ID'].tolist()))

# 添加顶部和底部节点
B.add_nodes_from(top_nodes, bipartite=0)
B.add_nodes_from(bottom_nodes, bipartite=1)

# 添加连接顶部和底部节点的边，包括时间戳和权重
edges = [(row['证券代码'], row['人员ID'], {'日期': row['日期'], '权重': row['权重']}) for idx, row in df.iterrows()]
B.add_edges_from(edges)

# 打印节点和边的数量
# print(nx.info(B))

# 打印顶部和底部节点列表
print('Top nodes:', B.nodes(0))
print('Bottom nodes:', B.nodes(1))

# 打印连接顶部和底部节点的边
for u, v, data in B.edges(data=True):
    print(u, v, data)