import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# 获取节点位置
pos = nx.spring_layout(G)

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_color='lightblue')

# 绘制边
nx.draw_networkx_edges(G, pos)

# 绘制节点标签
nx.draw_networkx_labels(G, pos, font_weight='bold')

plt.show()
