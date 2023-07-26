import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain
import torch
from torch_geometric.data import InMemoryDataset, Data
import pandas as pd

# xlsx = ['ding2.xlsx', 'di.xlsx', 'erbu.xlsx']
xlsx = ['ding2_100.xlsx', 'di100.xlsx', 'erbu100.xlsx']
# 读取顶部节点
ding_df = pd.read_excel(xlsx[0])
ding_code = ding_df['股票代码'].tolist()
ding_year = ding_df['年份'].tolist()

# 读取底部节点
di_df = pd.read_excel(xlsx[1])
di_year = di_df['年份'].tolist()
di_id = di_df['人员ID'].tolist()

# 读取边信息
erbu_df = pd.read_excel(xlsx[2])
erbu_code = erbu_df['证券代码'].tolist()
erbu_id = erbu_df['人员ID'].tolist()
erbu_year = erbu_df['年份'].tolist()
erbu_weight = erbu_df['权重'].tolist()

erbu_edge_id_year = list(zip(erbu_id, erbu_year))
erbu_edge_code_year = list(zip(erbu_code, erbu_year))


# build a graph
G = nx.Graph()
# edgelist = [(0, 1), (0, 2), (1, 3)]  # note that the order of edges
# G.add_edges_from(edgelist)
G.add_nodes_from(ding_code)
G.add_nodes_from(ding_year)

G.add_nodes_from(di_id)
G.add_nodes_from(di_year)

G.add_edges_from(erbu_edge_id_year)
G.add_edges_from(erbu_edge_code_year)


# plot the graph
# fig, ax = plt.subplots(figsize=(4,4))
# option = {'font_family':'serif', 'font_size':'15', 'font_weight':'semibold'}
# nx.draw_networkx(G, node_size=400, **option)  #pos=nx.spring_layout(G)
# plt.axis('off')
# plt.show()



x = torch.eye(G.number_of_nodes(), dtype=torch.float)

adj = nx.to_scipy_sparse_matrix(G).tocoo()
row = torch.from_numpy(adj.row.astype(np.int64)).to(torch.long)
col = torch.from_numpy(adj.col.astype(np.int64)).to(torch.long)
edge_index = torch.stack([row, col], dim=0)

# Compute communities.
partition = community_louvain.best_partition(G)
for i in range(G.number_of_nodes()):
    print(i)

# y = torch.tensor([partition[i] for i in range(G.number_of_nodes())])

# Select a single training node for each community
# (we just use the first one).
train_mask = torch.zeros(y.size(0), dtype=torch.bool)
for i in range(int(y.max()) + 1):
    train_mask[(y == i).nonzero(as_tuple=False)[0]] = True

data = Data(x=x, edge_index=edge_index, y=y, train_mask=train_mask)


import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = GCNConv(data.num_node_features, 16)
        self.conv2 = GCNConv(16, 2)

    def forward(self):
        x, edge_index = data.x, data.edge_index

        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index)

        return F.log_softmax(x, dim=1)

device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
model, data = Net().to(device), data.to(device)
optimizer = torch.optim.Adam([
    dict(params=model.conv1.parameters(), weight_decay=5e-4),
    dict(params=model.conv2.parameters(), weight_decay=0)
], lr=0.01)  # Only perform weight-decay on first convolution.

def train():
    optimizer.zero_grad()  
    out = model()
    loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
    
def test():
    model.eval()
    logits, accs = model(), []
    for _, mask in data('train_mask', 'test_mask'):
        pred = logits[mask].max(1)[1]
        acc = pred.eq(data.y[mask]).sum().item() / mask.sum().item()
        accs.append(acc)
    return accs


for epoch in range(1, 11):
    train()
    log = 'Epoch: {:03d}, Train: {:.4f}, Test: {:.4f}'
    print(log)
    # print(log.format(epoch, *test()))

