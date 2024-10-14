import pandas as pd
import matplotlib.pyplot as plt

# 使用债券代码、'Sperchge', 'Cnvtvalu', 'Cvtprmrt'四个因子进行训练
# 使用普通模型

# 加载数据
df = pd.read_excel('predictions_with_trddt.xlsx')
df2 = pd.read_excel('predictions_with_trddt-line.xlsx')

# 确保时间列是日期格式
df['Trddt'] = pd.to_datetime(df['Trddt'])
df2['Trddt'] = pd.to_datetime(df2['Trddt'])

# 假设 df 和 df2 的 Trddt 列是匹配的，直接绘制
plt.figure(figsize=(10, 6))

# 绘制 df 的 MSE
plt.plot(df['Trddt'], df['MSE'], label='MAPE - RandomForestRegressor', color='b')

# 绘制 df2 的 MSE
plt.plot(df2['Trddt'], df2['MSE'], label='MAPE - LinearRegression', color='g', linestyle='--')

# 设置标题和标签
plt.title('MAPE Comparison over Time')
plt.xlabel('Date')
plt.ylabel('MAPE')

# 显示图例
plt.legend()

# 旋转 x 轴日期标签
plt.xticks(rotation=45)

# 显示网格
plt.grid(True)

# 调整布局，避免标签重叠
plt.tight_layout()

# 显示图表
plt.show()
