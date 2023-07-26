import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain
import torch
from torch_geometric.data import InMemoryDataset, Data
import pandas as pd
import math

# 这个文件可以运行通过

# 完整的数据量太大了，截取前三十个数据作为测试样本
xlsx = ['ding2.xlsx', 'di.xlsx', 'erbu_all.xlsx']

# 测试样本呢
#xlsx = ['ding2_100.xlsx', 'di100.xlsx', 'erbu100.xlsx']

# ceshi
# xlsx = ['ding2_100.xlsx', 'di100.xlsx', 'erbu-1.xlsx']


# 读取边信息
erbu_df = pd.read_excel(xlsx[2], converters={'证券代码':str, '人员ID':str})
erbu_code = erbu_df['证券代码'].tolist()
erbu_id = erbu_df['人员ID'].tolist()
erbu_year = erbu_df['年份'].tolist()
erbu_weight = erbu_df['权重'].tolist()
print(erbu_df)
erbu_code_set = set(erbu_code)


result = erbu_df.groupby(['证券代码', '人员ID']).size()
print(result)
print(isinstance(result,pd.DataFrame))
print(isinstance(result,pd.Series))
print(result['000001', '30124574'])
print(result['000001', '30124574'])

for i in erbu_df.index:
    # temp = result[erbu_df['证券代码'][i], erbu_df['人员ID'][i]]
    
    # 计算指数权重
    erbu_df['权重'][i] = math.pow(2, result[erbu_df['证券代码'][i], erbu_df['人员ID'][i]])
    
    # 计算对数权重
    # erbu_df['权重'][i] = math.log(result[erbu_df['证券代码'][i], erbu_df['人员ID'][i]], 2)

erbu_df.to_excel(excel_writer='erbu_all_weight_pow.xlsx', sheet_name='sheet_1')

#

erbu_edge_id_year = list(zip(erbu_id, erbu_year, erbu_weight))
erbu_edge_code_year = list(zip(erbu_code, erbu_year, erbu_weight))