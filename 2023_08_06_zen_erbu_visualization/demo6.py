import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 这个文件画出来的图是一类节点作为内环，一类节点作为外环

xlsx_names = ['data/di_year2009_com0_20.xlsx', 
              'data/ding_year2009_com0_20.xlsx', 
              'data/erbu_year2009_com0_20.xlsx']

di = pd.read_excel(xlsx_names[0], usecols=['人员ID'])
ding = pd.read_excel(xlsx_names[1], usecols=['股票代码'])
erbu = pd.read_excel(xlsx_names[2], usecols=['证券代码', '人员ID'])

di
ding

di.size
ding.size

outer_nodes = di['人员ID'].to_list()
inner_nodes = ding['股票代码'].to_list()
erbu_data = list(zip(erbu['证券代码'], erbu['人员ID']))


# 创建一个无向图
G = nx.Graph()

# 添加节点到内环
G.add_nodes_from(inner_nodes, ring='inner')
# 添加节点到外环
G.add_nodes_from(outer_nodes, ring='outer')
# 添加边连接内环和外环的节点
G.add_edges_from(erbu_data)

# 绘制图形 scale调整节点之间的距离。增加 scale 的值会使节点之间的距离更大。
pos = nx.shell_layout(G, nlist=[inner_nodes, outer_nodes], scale=10)

# 绘制图形

nx.draw_networkx_edges(G, pos)
plt.legend()
plt.show()
