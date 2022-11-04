import os
from tempfile import tempdir
import pandas as pd
import numpy as np

# 读取降水量
filePath = r"/Volumes/roczhang/model-data/climate/"
nameList = os.listdir(filePath)

data = []
dfSum = pd.DataFrame(columns=['降水量(mm)'])  #先构建一个空的数据框
for i in nameList:
    if i.endswith('.xls'):
        absFilePath = filePath + i
        df = pd.read_excel(absFilePath, index_col=[4, 5])
        # temp = df[['年份', '月份', '降水量(mm)']]
        temp = df[['降水量(mm)']]
        dfSum = pd.concat([dfSum, temp])

print(dfSum)
print(df['降水量(mm)'].dtype)