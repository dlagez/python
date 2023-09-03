import pandas as pd
import numpy as np
import torch

# 提取节点特征列，假设特征列的名称为 'Feature1'、'Feature2'、'Feature3' 等
# 读取节点信息
tag_file = r'data/top100 with tag.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
tag_df = pd.read_excel(tag_file)
tag_df.info()
tag_feature_columns = ['股票代码', '年份', '资产负债率', '营业收入增长率A']  # 根据实际列名替换
tag_your_node_features = tag_df[tag_feature_columns].to_numpy()
tag_node_features = torch.tensor(tag_your_node_features, dtype=torch.float32)

tag_flag_your_node_features = tag_df['违规公司'].to_numpy()
tag_flag_your_node_features.shape
tag_flag_node_features = torch.tensor(tag_flag_your_node_features, dtype=torch.float32)

# 读取人的节点信息
di_file = r'data/top 100 di.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
di_df = pd.read_excel(di_file)
# data_types = {'职务类别': int}
# di_df = di_df.astype(data_types)
di_feature_columns = ['人员ID', '年份', '是否领取薪酬', '年龄']  # 根据实际列名替换
di_your_node_features = di_df[di_feature_columns].to_numpy()
di_df.info()
di_your_node_features.shape
di_node_features = torch.tensor(di_your_node_features, dtype=torch.float32)
di_flag = np.zeros((di_your_node_features.shape[0], 1))

# 读取边的节点信息
erbu_file = r'data/top 100 erbu.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
erbu_df = pd.read_excel(erbu_file)
erbu_feature_columns = ['证券代码', '人员ID']  # 根据实际列名替换
erbu_your_node_features = erbu_df[erbu_feature_columns].to_numpy()
erbu_node_features = torch.tensor(erbu_your_node_features, dtype=torch.float32)
