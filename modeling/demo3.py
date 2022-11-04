import os
from tempfile import tempdir
import pandas as pd
import numpy as np

# 读取降水量
filePath = r"/Volumes/roczhang/model-data/climate/"
nameList = os.listdir(filePath)

recipitation = pd.DataFrame(columns=['降水量(mm)'])  #先构建一个空的数据框
for i in nameList:
    if i.endswith('.xls'):
        absFilePath = filePath + i
        df = pd.read_excel(absFilePath, index_col=[4, 5])
        # temp = df[['年份', '月份', '降水量(mm)']]
        temp = df[['降水量(mm)']]
        recipitation = pd.concat([recipitation, temp])


filePath = r"/Volumes/roczhang/model-data/f4.xls"
evaporation = pd.read_excel(filePath, index_col=[0, 1])
evaporation = df['土壤蒸发量(mm)']

recEva = pd.concat([recipitation, evaporation], axis=1)
print(recEva)

