import pandas as pd
import matplotlib.pyplot as plt

# 读取 Excel 文件
file_path = 'data/2024-09-24-kzz/result/processed_data_20240924_152213.xlsx'
df = pd.read_excel(file_path)

# 筛选出特定 Liscd
liscd_values = [110034]  # 假设你要读取两个 Liscd
liscd_data = df[df['Liscd'].isin(liscd_values)]

# 转换 Trddt 列为日期格式
liscd_data['Trddt'] = pd.to_datetime(liscd_data['Trddt'])

# 打印筛选后的数据
print(liscd_data)

# 绘制 Clsprc 价格走势
plt.figure(figsize=(10, 5))
for liscd in liscd_values:
    subset = liscd_data[liscd_data['Liscd'] == liscd]
    plt.plot(subset['Trddt'], subset['Clsprc'], marker='o', markersize=5, label=f'Liscd {liscd}')

plt.title('Clsprc Price Trend for Multiple Liscds')
plt.xlabel('Date')
plt.ylabel('Clsprc Price')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
