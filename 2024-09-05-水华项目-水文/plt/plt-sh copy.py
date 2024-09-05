import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 直接将时间作为字符串，按顺序展示。

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取数据
data = pd.read_csv('data/sh/Book1.csv')

# 绘制图形
plt.figure(figsize=(14, 8))

plt.plot(data['时间'], data['氨氮(mg/L)'], label='氨氮(mg/L)', marker='o')
plt.plot(data['时间'], data['COD(mg/L)'], label='COD(mg/L)', marker='o')
plt.plot(data['时间'], data['总磷(mg/L)'], label='总磷(mg/L)', marker='o')

# 添加标题和标签
plt.title('时间 vs 氨氮、COD、总磷浓度')
plt.xlabel('时间')
plt.ylabel('浓度 (mg/L)')
plt.xticks(rotation=45)  # 旋转X轴刻度标签，以便更好地显示
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
