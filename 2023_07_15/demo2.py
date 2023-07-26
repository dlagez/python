import networkx as nx
import pandas as pd
from datetime import datetime

# 读取Excel文件
df = pd.read_excel('tu.xlsx', sheet_name='Sheet1')
df['timestamp'] = df['日期'].apply(lambda x: int(datetime.strptime(str(x), '%Y').timestamp()))

# 创建一个空的有向图
T = nx.DiGraph()
top_nodes = list(set(df['证券代码'].tolist()))
bottom_nodes = list(set(df['人员ID'].tolist()))

# 添加节点
T.add_nodes_from(top_nodes, bipartite=0)
T.add_nodes_from(bottom_nodes, bipartite=1)
for idx, row in df.iterrows():
     # 获取源节点、目标节点、边权重和时间戳
     source = row['证券代码']
     target = row['人员ID']
     weight = row['权重']
     timestamp = row['timestamp']
     # 向图中添加边和边权重
     T.add_edge(source, target, weight=weight, timestamp=timestamp)
     degree_centrality = nx.algorithms.centrality.temporal_degree_centrality(T, weight='weight')
     for node, centrality in degree_centrality.items():
          print(node, centrality)