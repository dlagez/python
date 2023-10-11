import pandas as pd
import numpy as np
import torch

# 提取节点特征列，假设特征列的名称为 'Feature1'、'Feature2'、'Feature3' 等
# 读取节点信息
tag_file = r'data/top100 with tag.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
erbu_file = r'data/top 100 erbu.xlsx'
tag_df = pd.read_excel(tag_file)
tag_df.info()
tag_df.head(5)


erbu_df = pd.read_excel(erbu_file)
erbu_df.info()


code = [5, 2]
year = [2016, 2009]

# 找到违规公司
tag1 = tag_df.loc[tag_df['违规公司'].isin([1]) & tag_df['股票代码'].isin(code) & tag_df['年份'].isin(year), :]
tag1.head(5)
tag1.info()


person_set = set()

for index, row in tag1.iterrows():
    code = row['股票代码']
    year = row['年份']
    person_df = erbu_df[(erbu_df['证券代码'] == code) & (erbu_df['年份'] == year)]
    person_tuple = tuple(person_df['人员ID'].to_numpy())
    person_set.add(person_tuple)



