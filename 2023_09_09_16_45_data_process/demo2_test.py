import pandas as pd
import numpy as np
import torch

# 提取节点特征列，假设特征列的名称为 'Feature1'、'Feature2'、'Feature3' 等
# 读取节点信息
tag_file = r'c:\Users\roc\OneDrive\Documents\05 WHPU\zen\data\原始数据拷贝\Copy of tag.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
erbu_file = r'c:\Users\roc\OneDrive\Documents\05 WHPU\zen\data\原始数据拷贝\erbu.xlsx'
tag_df = pd.read_excel(tag_file, dtype={"股票代码":int, '年份': int})
tag_df.info()


# 找到违规公司
tag1 = tag_df.loc[tag_df['违规公司'].isin([1]) & tag_df['股票代码'].isin([5, 2]) & tag_df['年份'].isin([2016, 2009]), :]
# 有了违规公司的股票代码和违规年份
# 行不通
tag1_code_numpy = tag1['股票代码'].to_numpy()
tag1_code_numpy = tag1['年份'].to_numpy()
type(tag1)

print("如果有符合条件的违规公司，下面会显示的公司在指定年份的信息")
if len(tag1) > 1:
    tag1.sample(2)
elif len(tag1) == 1:
    tag1.sample(1)

erbu_df = pd.read_excel(erbu_file)
erbu_df.info()

# 筛选出指定年份违规公司的高管

person_set = set()

for index, row in tag1.iterrows():
    code = row['股票代码']
    year = row['年份']
    person_df = erbu_df.loc[erbu_df['证券代码'].isin([code]) & erbu_df['年份'].isin([year])]
    person_numpy = person_df['人员ID'].to_numpy()
    person_set.update(person_numpy.tolist())


len(person_set)
