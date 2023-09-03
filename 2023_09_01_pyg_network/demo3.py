import pandas as pd
import numpy as np
import torch
from torch_geometric.data import InMemoryDataset, Data
# 创建数据集

class CustomDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(CustomDataset, self).__init__(root, transform, pre_transform)
        self.data = None  # 用于存储数据

    def _download(self):
        # 这里可以放置下载数据的代码（如果需要）
        pass

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
        

        # 定义人节点信息
        di_file = r'data/top 100 di.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
        di_df = pd.read_excel(di_file)
        di_feature_columns = ['人员ID', '年份', '职务类别', '年龄']  # 根据实际列名替换
        di_your_node_features = di_df[di_feature_columns].to_numpy()
        di_node_features = torch.tensor(di_your_node_features, dtype=torch.float32)
        # flag
        di_flag = np.zeros((di_your_node_features.shape[0], 1))


        # 拼接节点信息
        feature_result = torch.vstack((tag_node_features, di_node_features))
        # 拼接标签信息
        flag_result = np.vstack((tag_flag_your_node_features, di_flag))

        x = feature_result
        y = flag_result


        # 定义边信息
        erbu_file = r'data/top 100 erbu.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
        erbu_df = pd.read_excel(erbu_file)
        erbu_feature_columns = ['股票代码', '人员ID'] # 根据实际列名替换
        erbu_your_node_features = erbu_df[erbu_feature_columns].to_numpy()
        edge_index = torch.tensor(erbu_your_node_features, dtype=torch.float32)



        # edge_index = torch.tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        #                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]], dtype=torch.long)  # 边索引
        # 创建一个 PyG Data 对象
        data = Data(x=x, y=y, edge_index=edge_index)

        self.data = data

# 创建自定义数据集
dataset = CustomDataset(root='/tmp/Custom', transform=None, pre_transform=None)

# 访问数据集的属性
print("数据集名称:", dataset.name)
print("数据集大小:", len(dataset))
print("第一个数据的节点特征:", dataset[0].x)
print("第一个数据的边索引:", dataset[0].edge_index)
print("第一个数据的标签:", dataset[0].y)
