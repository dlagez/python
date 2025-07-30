import pandas as pd
import os

# 文件路径（请根据实际路径修改）
file_path = r'D:\Download\dayu5000\项目金额和结算情况.xlsx'  # 替换为你的文件路径
output_path = r'D:\Download\dayu5000\项目金额和结算情况2.xlsx'  # 可选：另存为新文件

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 将“合同金额”转为万元单位，取整数，去负号
df['合同金额'] = df['合同金额'].abs()  # 去掉负号
df['合同金额'] = (df['合同金额'] / 10000).astype(int)  # 转万元并保留整数

# 保存结果
df.to_excel(output_path, index=False)

print("转换完成，文件保存至：", output_path)
