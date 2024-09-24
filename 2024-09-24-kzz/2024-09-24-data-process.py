import pandas as pd
import numpy as np
from datetime import datetime

# 读取数据
df = pd.read_excel('data/2024-09-24-kzz/raw/BND_Cbdrpch.xlsx')

# 将Trddt转换为日期格式
df['Trddt'] = pd.to_datetime(df['Trddt'])

# 按Liscd分组
grouped = df.groupby('Liscd')

# 存储处理后的数据
processed_data = []

# 基准代码
base_code = 110043

# 获取基准代码的所有交易日期
base_dates = df[df['Liscd'] == base_code]['Trddt'].unique()

for name, group in grouped:
    if len(group) < 223:
        # 删除该Liscd所有记录
        continue

    # 获取缺失日期
    missing_dates = set(base_dates) - set(group['Trddt'])

    median_values = {
        'Opnprc': group['Opnprc'].median(),
        'Clsprc': group['Clsprc'].median(),
        'Sperchge': group['Sperchge'].median(),
        'Cnvtvalu': group['Cnvtvalu'].median(),
        'Cvtprmrt': group['Cvtprmrt'].median(),
    }
    
    for missing_date in missing_dates:
        # 插入缺失数据
        new_row = {
            'Liscd': name,
            'Sctcd': group['Sctcd'].iloc[0],
            'Trddt': missing_date,
            'Opnprc': median_values['Opnprc'],
            'Clsprc': median_values['Clsprc'],
            'Sperchge': median_values['Sperchge'],
            'Cnvtvalu': median_values['Cnvtvalu'],
            'Cvtprmrt': median_values['Cvtprmrt'],
            'filled': '填充数据'  # 标记为填充数据
        }
        
        processed_data.append(new_row)

    # 保留原始数据并标记
    for _, row in group.iterrows():
        row_dict = row.to_dict()  # 转换为字典
        row_dict['filled'] = '原始数据'
        processed_data.append(row_dict)
    
# 创建处理后的 DataFrame
processed_df = pd.DataFrame(processed_data)
data/2024-09-24-kzz/result/processed_data_20240924_152213.xlsx
processed_df.sort_values(by=['Liscd', 'Trddt'], inplace=True)
# 备用使用全局的中位数填充
# 使用中位数填充缺失数据
# for column in ['Opnprc', 'Clsprc', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']:
#     median_value = processed_df[column].median()
#     processed_df[column].fillna(median_value, inplace=True)

# 保存处理后的数据到新的 Excel 文件
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f'data/2024-09-24-kzz/result/processed_data_{current_time}.xlsx'
processed_df.to_excel(output_filename, index=False)

