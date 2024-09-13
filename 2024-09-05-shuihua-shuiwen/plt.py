import matplotlib.pyplot as plt
import numpy as np

# SVM模型结果
svm_results = {
    'precision': [0.75, 0.80],
    'recall': [0.75, 0.80],
    'f1-score': [0.75, 0.80],
    'accuracy': [0.78]
}

# 假设 BP 模型结果
bp_results = {
    'precision': [0.75, 0.80],
    'recall': [0.75, 0.80],
    'f1-score': [0.75, 0.80],
    'accuracy': [0.78]
}

labels = ['Class 0', 'Class 1', 'Overall']
metrics = ['precision', 'recall', 'f1-score', 'accuracy']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()

for i, metric in enumerate(metrics):
    if metric != 'accuracy':
        svm_values = svm_results[metric] + [np.mean(svm_results[metric])]
        bp_values = bp_results[metric] + [np.mean(bp_results[metric])]
    else:
        svm_values = svm_results[metric]
        bp_values = bp_results[metric]

    ax = axs[i]
    rects1 = ax.bar(x - width/2, svm_values, width, label='SVM')
    rects2 = ax.bar(x + width/2, bp_values, width, label='BP')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(metric.capitalize())
    ax.set_title(f'{metric.capitalize()} by model and class')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    for rects in [rects1, rects2]:
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(round(height, 2)),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

fig.tight_layout()

plt.show()