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
plt.figure(figsize=(16, 10))

# 绘制数值数据
plt.plot(data['时间'], data['氨氮(mg/L)'], label='氨氮(mg/L)', marker='o')
plt.plot(data['时间'], data['COD(mg/L)'], label='COD(mg/L)', marker='o')
plt.plot(data['时间'], data['总磷(mg/L)'], label='总磷(mg/L)', marker='o')
plt.plot(data['时间'], data['气温（℃）'], label='气温（℃）', marker='o')
plt.plot(data['时间'], data['相对湿度（%）'], label='相对湿度（%）', marker='o')
plt.plot(data['时间'], data['降雨量（mm）'], label='降雨量（mm）', marker='o')
plt.plot(data['时间'], data['风速（km/h）'], label='风速（km/h）', marker='o')
plt.plot(data['时间'], data['光照时长（h）'], label='光照时长（h）', marker='o')

# 在图上标注“是否有蓝藻”
# for i, txt in enumerate(data['是否有蓝藻']):
#     plt.annotate(txt, (data['时间'][i], data['氨氮(mg/L)'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(data['是否有蓝藻']):
    plt.text(data['时间'][i], plt.ylim()[1] * 0.75 , txt, ha='center')

# 添加标题和标签
plt.title('时间 vs 各项指标')
plt.xlabel('时间')
plt.ylabel('数值')
plt.xticks(rotation=45)  # 旋转X轴刻度标签
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
