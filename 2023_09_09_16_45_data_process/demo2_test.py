import pandas as pd
import numpy as np
import torch

# 提取节点特征列，假设特征列的名称为 'Feature1'、'Feature2'、'Feature3' 等
# 读取节点信息
tag_file = r'c:\Users\roc\OneDrive\Documents\05 WHPU\zen\data\原始数据拷贝\Copy of tag.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
erbu_file = r'c:\Users\roc\OneDrive\Documents\05 WHPU\zen\data\原始数据拷贝\erbu.xlsx'
tag_df = pd.read_excel(tag_file, dtype={"股票代码":int, '年份': int})
tag_df.info()

code_list = [5, 2]
year_list = [2016, 2009]
year_target = 2010

# 找到违规公司
tag1 = tag_df.loc[tag_df['违规公司'].isin([1]) & tag_df['股票代码'].isin(code_list) & tag_df['年份'].isin(year_list), :]
# 有了违规公司的股票代码和违规年份
# 行不通
tag1_code_numpy = tag1['股票代码'].to_numpy()
tag1_code_numpy = tag1['年份'].to_numpy()
type(tag1)



erbu_df = pd.read_excel(erbu_file)
erbu_df.info()

# 筛选出指定年份违规公司的高管

person_set = set()
personDf_list = []

print("查询指定年份舞弊公司下的高管....")
for index, row in tag1.iterrows():
    code = row['股票代码']
    year = row['年份']
    person_df = erbu_df.loc[erbu_df['证券代码'].isin([code]) & erbu_df['年份'].isin([year])]
    personDf_list.append(person_df)
    person_numpy = person_df['人员ID'].to_numpy()
    person_set.update(person_numpy.tolist())

result = pd.concat(personDf_list)

company_list = []
# 如果有符合条件的公司，并且高管人数大于0
if len(result) > 0:
    for index, row in result.iterrows():
        id = row['人员ID']
        year = row['年份']
        company_df = erbu_df.loc[erbu_df['人员ID'].isin(id) & erbu_df['年份'].isin(year)]
        company_list.append(company_df)

company_result = pd.concat(company_list)


len(person_set)
print("找到的舞弊公司高管的id如下")
print(person_set)
print()
print("找到的舞弊公司如下:")
print("如果有符合条件的违规公司，下面会显示的公司在指定年份的信息")
if len(tag1) > 5:
    tag1.sample(5)
elif len(tag1) > 1:
    tag1.sample(1)

print('找到符合条件指定年份的公司如下')
company_result.sample(1)