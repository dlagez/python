import os
from tempfile import tempdir
import pandas as pd
import numpy as np

# 读取蒸发量
filePath = r"/Volumes/roczhang/model-data/f4.xls"

df = pd.read_excel(filePath, index_col=[0, 1])
df = df['土壤蒸发量(mm)']
print(df)