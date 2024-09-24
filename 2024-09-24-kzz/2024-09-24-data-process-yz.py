import pandas as pd
import os

# 读取处理完成的文件
# file_path = 'data/2024-09-24-kzz/result/processed_data_20240924_152213.xlsx'
file_path = 'data/2024-09-24-kzz/raw/BND_Cbdrpch.xlsx'
df = pd.read_excel(file_path)

# 按 Liscd 分组并统计每组的条目数
grouped_stats = df.groupby('Liscd').size().reset_index(name='Count')

# 显示统计结果
print(grouped_stats)

# 获取原始文件的名称并添加 "_status"
base_name = os.path.basename(file_path)  # 获取原始文件名
name, ext = os.path.splitext(base_name)  # 分离文件名和扩展名
output_stats_path = f'data/2024-09-24-kzz/result/{name}_status{ext}'  # 生成新的文件名

# 保存统计结果
grouped_stats.to_excel(output_stats_path, index=False)
