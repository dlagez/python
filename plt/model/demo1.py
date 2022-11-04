import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  

filePath = r"/Volumes/roczhang/model-data/b14.xlsx"

df = pd.read_excel(filePath, index_col=0)
df_g17 = df[df['小区'] == 'G17']


# df_g17 = df['SOC土壤有机碳']

print(df)

df_g17.plot.bar()


print(df)