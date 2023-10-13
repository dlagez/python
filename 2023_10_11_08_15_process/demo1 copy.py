import pandas as pd
import numpy as np

# ---------第一步：读取excel表格------------
# 提取节点特征列，假设特征列的名称为 'Feature1'、'Feature2'、'Feature3' 等
# 读取节点信息
tag_cols = ['证券代码', '公告日', '财务违规']
# tag_types = {'证券代码': str, '公告日': str, '财务违规': str}
tag_file = r'data/tag.xlsx'  # 将 'your_data.xlsx' 替换为你的 Excel 文件路径
tag_df = pd.read_excel(tag_file, engine='openpyxl', usecols=tag_cols)
tag_df.info()
tag_df.head(5)

erbu_cols = ['证券代码', '人员ID', '年份']
# erbu_types = {'证券代码': str, '人员ID': str, '年份': str}
erbu_file = r'data/erbu.xlsx'
erbu_df = pd.read_excel(erbu_file, engine='openpyxl', usecols=erbu_cols)
erbu_df.info()

# -------------选取公司，年份来获取舞弊人员-----------
code = [5, 2, 7, 9, 10, 11, 12]
year = [2016, 2017, 2018]
# ------------定义年份，找到这个年份舞弊人员对应的公司-----------
target_year=2013

# ---------------通过公司代码和年份获取违规公司对应的人---------------
tag1 = tag_df.loc[tag_df['财务违规'].isin([1]) & tag_df['证券代码'].isin(code) & tag_df['公告日'].isin(year), :]
tag1.head(5)
tag1.head(20)

tag1.info()

# ----------------将人的id提取出来，存入set集合里面，并去重-----------------
person_set = set()
person_set
# 获取到人员id的集合。
for index, row in tag1.iterrows():
    code = row['证券代码']
    year = row['公告日']
    person_df = erbu_df[(erbu_df['证券代码'] == code) & (erbu_df['年份'] == year)]
    person_tuple = set(person_df['人员ID'].to_numpy())
    person_set.update(person_tuple)


# company_df = erbu_df.loc[(erbu_df['年份'] == target_year) & (erbu_df['人员ID'] == 30114570)]
# 根据人员id和指定的年份获得指定的公司。
# company_code = company_df['证券代码'].iloc[0]
# company_code_list.append(company_code)

# ---------------------通过年份和违规人员id获取指定年份违规人员所对应的公司。----------------------------
company_code_list = []
for i in person_set:
    # company = erbu_df.loc[(erbu_df['年份'] == target_year) & erbu_df['人员ID'].isin(person_set)]
    company_df = erbu_df.loc[(erbu_df['年份'] == target_year) & (erbu_df['人员ID'] == i)]
    if not company_df.empty:
        company_code = company_df['证券代码'].iloc[0]
        company_code_list.append(company_code)
#--------------------打印指定年份违规人员所对应的公司----------------------------
print(company_code_list)
