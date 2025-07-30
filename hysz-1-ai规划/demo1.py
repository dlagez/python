import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 一阶段工作计划（Ai辅助员工）2026年
# 1、数据资产化建设。10% 
# 2、流程标准化建设。 10% 
# 3、人才智能化建设。  30% 
# 二阶段工作计划（Ai与员工 工作对半分）（2027年-2028年）
# 1、数据资产化建设。30% 
# 2、流程标准化建设。 30% 
# 3、人才智能化建设。  60%  
# 三阶段计划（员工辅助ai工作）（2029年-2030年）
# 1、数据资产化建设。100% 
# 2、流程标准化建设。 100% 
# 3、人才智能化建设。  100%  
# 给我一个python代码，我用可视化方法来展示这个计划。


# 设置中文和图形参数
rcParams['font.sans-serif'] = ['Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

# 阶段与数据
phases = ['2026', '2027-2028', '2029-2030']
data_asset = [10, 30, 100]
process_std = [10, 30, 100]
talent_ai = [30, 60, 100]

x = np.arange(len(phases))
bar_width = 0.25
x1 = x - bar_width
x2 = x
x3 = x + bar_width

# 更现代的颜色方案（轻盈渐变色）
colors = ['#6EC1E4', '#F4A261', '#2A9D8F']

# 创建图像，设置白底和高清晰度
fig, ax = plt.subplots(figsize=(10, 8), dpi=120)
fig.patch.set_facecolor('white')

# 添加网格线提升现代感
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# 去掉上右边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# 绘制柱状图（圆角）
bars1 = ax.bar(x1, data_asset, width=bar_width, label='数据资产化建设', color=colors[0], edgecolor='none')
bars2 = ax.bar(x2, process_std, width=bar_width, label='流程标准化建设', color=colors[1], edgecolor='none')
bars3 = ax.bar(x3, talent_ai, width=bar_width, label='人才智能化建设', color=colors[2], edgecolor='none')

# 设置标题与坐标轴样式
ax.set_title('三大建设进度（2026-2030）', fontsize=18, fontweight='bold')
ax.set_xlabel('时间阶段', fontsize=12)
ax.set_ylabel('推进程度（%）', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(phases, fontsize=11)
ax.set_ylim(0, 140)

# 图例美化
ax.legend(loc='upper left', fontsize=11, frameon=False)

# 添加圆角（让柱子不那么“死板”）
def round_bar(bar):
    for rect in bar:
        height = rect.get_height()
        rect.set_linewidth(0)
        rect.set_path_effects([])
        rect.set_clip_on(False)
        rect.set_joinstyle('round')

round_bar(bars1)
round_bar(bars2)
round_bar(bars3)

# 添加数据标签（上移 + 加粗）
for i in range(len(phases)):
    ax.text(x1[i], data_asset[i] + 5, f"{data_asset[i]}%", ha='center', fontsize=10, weight='bold')
    ax.text(x2[i], process_std[i] + 5, f"{process_std[i]}%", ha='center', fontsize=10, weight='bold')
    ax.text(x3[i], talent_ai[i] + 5, f"{talent_ai[i]}%", ha='center', fontsize=10, weight='bold')

plt.tight_layout()
plt.show()
