import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain
import torch
from torch_geometric.data import InMemoryDataset, Data
import pandas as pd
import math

erbu_df = pd.read_excel('demo3.xlsx', converters={'证券代码':str, '人员ID':str, '年份':str})
G = nx.Graph()

erbu_code = erbu_df['证券代码'].tolist()
erbu_id = erbu_df['人员ID'].tolist()
erbu_year = erbu_df['年份'].tolist()
erbu_weight = erbu_df['权重'].tolist()

erbu_edge_code_year = list(zip(erbu_code, erbu_year, erbu_weight))
G.add_weighted_edges_from(erbu_edge_code_year)
result = nx.degree_centrality(G)
result