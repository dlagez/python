import matplotlib.pyplot as plt

# 传统：60%事务性 + 30%沟通 + 10%分析

# AI后：20%事务性 + 30%沟通 + 50%分析


# 设置字体（防止中文乱码）
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['事务性工作', '沟通协作', '分析与决策']
traditional = [60, 30, 10]
ai_enabled = [20, 30, 50]

colors = ['#f4b183', '#a9d18e', '#9dc3e6']

# 创建子图
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('传统模式 vs AI赋能后：员工时间分布对比', fontsize=14)

# 绘制传统模式饼图
axs[0].pie(traditional, labels=labels, autopct='%1.0f%%', startangle=90, colors=colors)
axs[0].set_title('传统模式')

# 绘制AI赋能后饼图
axs[1].pie(ai_enabled, labels=labels, autopct='%1.0f%%', startangle=90, colors=colors)
axs[1].set_title('AI赋能后')

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()