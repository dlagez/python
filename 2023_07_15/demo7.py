import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain
import torch
from torch_geometric.data import InMemoryDataset, Data
import pandas as pd

# 这个文件可以运行通过

# 完整的数据量太大了，截取前三十个数据作为测试样本
# xlsx = ['ding2.xlsx', 'di.xlsx', 'erbu.xlsx']

# 测试样本呢
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

erbu_edge_id_year = list(zip(erbu_id, erbu_year, erbu_weight))
erbu_edge_code_year = list(zip(erbu_code, erbu_year, erbu_weight))


# build a graph
G = nx.Graph()
# edgelist = [(0, 1), (0, 2), (1, 3)]  # note that the order of edges
# G.add_edges_from(edgelist)

G.add_nodes_from(ding_code)
G.add_nodes_from(ding_year)

G.add_nodes_from(di_id)
G.add_nodes_from(di_year)

# 如果边不带权重，使用下面的代码
# G.add_edges_from(erbu_edge_id_year)
# G.add_edges_from(erbu_edge_code_year)

# 如果边带权重，使用下面的代码
G.add_weighted_edges_from(erbu_edge_id_year)
G.add_weighted_edges_from(erbu_edge_code_year)

x = torch.ones((G.number_of_nodes(),1), dtype=torch.float)
adj = nx.to_scipy_sparse_array(G).tocoo()

# 获取非零元素行索引
row = torch.from_numpy(adj.row.astype(np.int64)).to(torch.long)
# 获取非零元素列索引
col = torch.from_numpy(adj.col.astype(np.int64)).to(torch.long)

# 将行和列进行拼接，shape变为[2, num_edges], 包含两个列表，第一个是row, 第二个是col
edge_index = torch.stack([row, col], dim=0)

data = Data(x=x, edge_index=edge_index)

# 这个是将转化的图神经网络进行分类训练，目前还没有测试
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
    print(log.format(epoch, *test()))
