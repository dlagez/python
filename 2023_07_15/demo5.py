import torch
from torch_geometric.data import Data

# 一个无权无向图的示例
# 边的索引 COO格式 就是说第一行代表行索引 第二行代表列索引
# 节点0和1之间有一条边；节点1和2之间有一条边 
edge_index = torch.tensor([[0, 1, 1, 2], 
                           [1, 0, 2, 1]], dtype=torch.long)
# 节点0 1 2的特征分别是
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index)
#>>> Data(x=[3, 1], edge_index=[2, 4])
