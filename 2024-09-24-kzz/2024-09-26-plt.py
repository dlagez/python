import pandas as pd
import matplotlib.pyplot as plt

# 读取 Excel 文件
file_path = 'data/2024-09-24-kzz/result/processed_data_20240924_152213.xlsx'
df = pd.read_excel(file_path)

# 筛选出特定 Liscd
liscd_data = df[df['Liscd'] == 110034]

# 转换 Trddt 列为日期格式
liscd_data['Trddt'] = pd.to_datetime(liscd_data['Trddt'])

# 绘制 Clsprc 价格走势
plt.figure(figsize=(10, 5))
plt.plot(liscd_data['Trddt'], liscd_data['Clsprc'], marker='o')
plt.title('Clsprc Price Trend for Liscd 110034')
plt.xlabel('Date')
plt.ylabel('Clsprc Price')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
