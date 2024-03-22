import networkx as nx

# 创建一个空的二模模型
G = nx.Graph()

# 添加左侧节点
G.add_node("User1", bipartite=0)
G.add_node("User2", bipartite=0)

# 添加右侧节点
G.add_node("Product1", bipartite=1)
G.add_node("Product2", bipartite=1)

# 添加边（连接左侧节点和右侧节点）
G.add_edge("User1", "Product1")
G.add_edge("User2", "Product1")
G.add_edge("User2", "Product2")

# 手动进行左侧投影
left_nodes = {node for node, data in G.nodes(data=True) if data["bipartite"] == 0}
left_projection = nx.Graph(G.subgraph(left_nodes))

# 查看左侧投影的边
print("Left Projection Edges:", left_projection.edges())