# from torch_geometric.datasets import Planetoid
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, SAGEConv, GATConv

import pandas as pd
import numpy as np
from torch_geometric.data import InMemoryDataset, Data


class CustomDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(CustomDataset, self).__init__(root, transform, pre_transform)
        self.data = None  # 用于存储数据

    def _download(self):
        # 这里可以放置下载数据的代码（如果需要）
        pass

    def raw_file_names(self):
        return ['aaa']

    def processed_file_names(self):
        return ['data']

    def process(self):
        # 这里可以对数据进行预处理
        # x = torch.randn(10, 16)  # 节点特征矩阵
        # y = torch.tensor([0, 1, 0, 1, 2, 2, 0, 1, 2, 1])  # 节点标签

        # 定义顶部节点信息
        tag_file = r'data/top100 with tag.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
        tag_df = pd.read_excel(tag_file)
        tag_feature_columns = ['股票代码', '年份', '资产负债率', '营业收入增长率A']  # 根据实际列名替换
        tag_your_node_features = tag_df[tag_feature_columns].to_numpy()
        tag_node_features = torch.tensor(tag_your_node_features, dtype=torch.float32)
        # flag
        tag_flag_your_node_features = tag_df['违规公司'].to_numpy()
        tag_flag_your_node_features.shape

        # 定义人节点信息
        di_file = r'data/top 100 di.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
        di_df = pd.read_excel(di_file)
        di_feature_columns = ['人员ID', '年份', '是否领取薪酬', '年龄']  # 根据实际列名替换
        di_your_node_features = di_df[di_feature_columns].to_numpy()
        # di_df.info()
        di_node_features = torch.tensor(di_your_node_features, dtype=torch.float32)
        # flag
        di_flag = np.zeros((di_your_node_features.shape[0]))
        # di_flag.shape


        # 拼接节点信息
        feature_result = torch.vstack((tag_node_features, di_node_features))
        feature_result = torch.tensor(feature_result, dtype=torch.float32)
        # 拼接标签信息
        flag_result = np.vstack((tag_flag_your_node_features, di_flag))
        flag_result = torch.tensor(flag_result, dtype=torch.float32)


        x = feature_result
        y = flag_result


        # 定义边信息
        erbu_file = r'data/top 100 erbu.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
        erbu_df = pd.read_excel(erbu_file)
        erbu_feature_columns = ['证券代码', '人员ID'] # 根据实际列名替换
        erbu_your_node_features = erbu_df[erbu_feature_columns].to_numpy()
        edge_index = torch.tensor(erbu_your_node_features, dtype=torch.float32)



        # edge_index = torch.tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        #                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]], dtype=torch.long)  # 边索引
        # 创建一个 PyG Data 对象
        data = Data(x=x, y=y, edge_index=edge_index)

        self.data = data

# dataset = Planetoid(root='/tmp/Cora', name='Cora')
dataset = CustomDataset(root='/tmp/Custom', transform=None, pre_transform=None)
dataset.data
class GAT_Net(torch.nn.Module):
    def __init__(self, features, hidden, classes, heads=1):
        super(GAT_Net, self).__init__()
        self.gat1 = GATConv(features, hidden, heads=heads)
        self.gat2 = GATConv(hidden * heads, classes)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.gat1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
        x = self.gat2(x, edge_index)
        return F.log_softmax(x, dim=1)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GAT_Net(4, 16, 2, heads=1).to(device)
data = dataset[0]
data



dataset.x
dataset.edge_index
dataset.num_classes
dataset.num_node_features
data.is_undirected()



# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
# optimizer = torch.optim.Adam([
# 	dict(params=model.conv1.parameters(), weight_decay=5e-4),
#     dict(params=model.conv2.parameters(), weight_decay=0)
#     ], lr=0.01)
optimizer = torch.optim.Adam(model.parameters(),
                             lr=0.01, weight_decay=5e-4)

model.train()
for epoch in range(1000):
    optimizer.zero_grad()
    out = model(data)
    loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
    correct = out[data.train_mask].max(dim=1)[1].eq(data.y[data.train_mask]).double().sum()
    # print('epoch:', epoch, ' acc:', correct / int(data.train_mask.sum()))
    loss.backward()
    optimizer.step()
    if epoch % 10 == 9:
        model.eval()
        logits, accs = model(data), []
        for _, mask in data('train_mask', 'val_mask', 'test_mask'):
            pred = logits[mask].max(1)[1]
            acc = pred.eq(data.y[mask]).sum().item() / mask.sum().item()
            accs.append(acc)
        log = 'Epoch: {:03d}, Train: {:.5f}, Val: {:.5f}, Test: {:.5f}'
        print(log.format(epoch + 1, accs[0], accs[1], accs[2]))



