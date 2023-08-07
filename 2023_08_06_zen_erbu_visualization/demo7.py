import networkx as nx
import matplotlib.pyplot as plt

# 创建一个无向图
G = nx.Graph()

# 添加节点到内环
inner_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
G.add_nodes_from(inner_nodes, ring='inner')  # 使用 'ring' 属性标识内环

# 添加节点到外环
outer_nodes = ['X', 'Y', 'Z', 'W', 'V', 'U', 'T', 'S', 'R', 'Q']
G.add_nodes_from(outer_nodes, ring='outer')  # 使用 'ring' 属性标识外环
# 添加边连接内环和外环的节点
edges = [('A', 'X'), ('B', 'Y'), ('C', 'Z'), ('D', 'W'), ('E', 'V'), ('F', 'U'), ('G', 'T'), ('H', 'S'), ('I', 'R'), ('J', 'Q')]
G.add_edges_from(edges)

pos = nx.shell_layout(G, nlist=[inner_nodes, outer_nodes], scale=2)

nx.draw_networkx_edges(G, pos)
plt.legend()
plt.show()
