import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 将时间转成时间格式，并在时间维度展示


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取数据
data = pd.read_csv('data/sh/Book1.csv')

# 将“时间”列转换为日期时间格式
data['时间'] = pd.to_datetime(data['时间'], format='%m月%d日', errors='coerce')
data['时间'] = pd.to_datetime(data['时间'], format='%m/%d', errors='coerce').fillna(data['时间'])
data['时间'] = pd.to_datetime(data['时间'], format='%Y/%m/%d', errors='coerce').fillna(data['时间'])

# 绘制图形
plt.figure(figsize=(14, 8))

plt.plot(data['时间'], data['氨氮(mg/L)'], label='氨氮(mg/L)', marker='o')
plt.plot(data['时间'], data['COD(mg/L)'], label='COD(mg/L)', marker='o')
plt.plot(data['时间'], data['总磷(mg/L)'], label='总磷(mg/L)', marker='o')

# 添加标题和标签
plt.title('时间 vs 氨氮、COD、总磷浓度')
plt.xlabel('时间')
plt.ylabel('浓度 (mg/L)')
plt.xticks(rotation=45)
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
