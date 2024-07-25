import matplotlib.pyplot as plt
import numpy as np

# BP模型结果
bp_results = {
    'precision': [1.00, 0.75],
    'recall': [0.50, 1.00],
    'f1-score': [0.67, 0.86],
    'accuracy': [0.80]
}

# SVM模型结果
svm_results = {
    'precision': [0.75, 0.80],
    'recall': [0.75, 0.80],
    'f1-score': [0.75, 0.80],
    'accuracy': [0.78]
}

# 随机森林模型结果
rf_results = {
    'precision': [0.33, 0.33],
    'recall': [0.50, 0.20],
    'f1-score': [0.40, 0.25],
    'accuracy': [0.33]
}

labels = ['Class 0', 'Class 1', 'Overall']
metrics = ['precision', 'recall', 'f1-score', 'accuracy']

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()

for i, metric in enumerate(metrics):
    if metric != 'accuracy':
        bp_values = bp_results[metric] + [np.mean(bp_results[metric])]
        svm_values = svm_results[metric] + [np.mean(svm_results[metric])]
        rf_values = rf_results[metric] + [np.mean(rf_results[metric])]
    else:
        bp_values = bp_results[metric]
        svm_values = svm_results[metric]
        rf_values = rf_results[metric]

    ax = axs[i]
    rects1 = ax.bar(x - width, bp_values, width, label='BP')
    rects2 = ax.bar(x, svm_values, width, label='SVM')
    rects3 = ax.bar(x + width, rf_values, width, label='RandomForest')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(metric.capitalize())
    ax.set_title(f'{metric.capitalize()} by model and class')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    for rects in [rects1, rects2, rects3]:
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(round(height, 2)),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

fig.tight_layout()

plt.show()
