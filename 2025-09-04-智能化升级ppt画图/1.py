import matplotlib.pyplot as plt
from matplotlib import rcParams

# 解决中文乱码
rcParams['font.sans-serif'] = ['SimHei']  
rcParams['axes.unicode_minus'] = False

# 数据
time_original = 10
time_ai = 1
processes_per_day = 10
workday_minutes = 4800

# ----------------- 柱状图 -----------------
plt.figure(figsize=(6,4))
plt.bar(["原流程", "AI流程"], [time_original, time_ai], color=["#63CF72","#D1E824"])
plt.title("单个流程审批耗时对比")
plt.ylabel("时间（分钟）")
for i, v in enumerate([time_original, time_ai]):
    plt.text(i, v + 0.2, str(v), ha='center', fontsize=12)
plt.show()

# ----------------- 饼状图 -----------------
# 原始审批总时间
total_time_original = time_original * processes_per_day
# AI 审批总时间
total_time_ai = time_ai * processes_per_day

# 饼图数据（占一天 4800 分钟的比例）
sizes_original = [total_time_original, workday_minutes - total_time_original]
sizes_ai = [total_time_ai, workday_minutes - total_time_ai]

labels = ["审批耗时", "其他工作"]

fig, axes = plt.subplots(1, 2, figsize=(10,5))

# 原流程饼图
axes[0].pie(sizes_original, labels=labels, autopct='%1.1f%%', colors=["#FF9999","#DDDDDD"])
axes[0].set_title("原流程耗时占比")

# AI流程饼图
axes[1].pie(sizes_ai, labels=labels, autopct='%1.1f%%', colors=["#66B3FF","#DDDDDD"])
axes[1].set_title("AI流程耗时占比")

plt.show()
