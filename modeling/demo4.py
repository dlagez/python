# q6
import pandas as pd
import matplotlib.pyplot as plt

filePath = r"/Volumes/roczhang/temp/Q4.all_data.xlsx"

df = pd.read_excel(filePath, index_col=0)
df_g17 = df[df['小区'] == 'G17']
