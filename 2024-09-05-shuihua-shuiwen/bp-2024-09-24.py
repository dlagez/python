import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from datetime import datetime

# 使用全量数据训练模型

# 假设数据已经加载到DataFrame中
data = pd.read_excel('data/sh/2024-09-24-data/sw.xls')

# 提取相关特征（假设已经有数据）
data.columns = ['时间', '风速', '降雨量', '相对湿度', '气温', '光照时长', '是否有水华']

# 选择所需的列
# data = df[['气温', '相对湿度', '降雨量', '风速', '光照时长']].values



# 特征和标签
features = data[['气温', '相对湿度', '降雨量', '风速', '光照时长']]
features
labels = data['是否有水华']
labels

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.1, random_state=42)

# 创建并训练BP神经网络模型
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(X_train, y_train)

# 预测
y_pred = mlp.predict(X_test)




# 评估模型
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)

# 保存模型
# 获取当前时间，格式为 YYYYMMDD_HHMMSS
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
joblib.dump(mlp, f'2024-09-05-shuihua-shuiwen/model2/mlp_model{current_time}_acc_{accuracy}.pkl')

# 实验结果怎么看
#               precision    recall  f1-score   support
#            0       0.90      0.81      0.85        16
#            1       0.83      0.92      0.87        12
#     accuracy                           0.86        28
#    macro avg       0.87      0.86      0.86        28
# weighted avg       0.87      0.86      0.86        28

# 类别 0 的 precision 是 0.90，这意味着在所有被预测为类别 0 的样本中，90% 是实际属于类别 0 的。
# 类别 0 的 recall 是 0.81，这意味着在所有实际属于类别 0 的样本中，81% 被正确预测为类别 0。
# 类别 0 的 f1-score 是 0.85，这是精度和召回率的调和平均数。
# 类别 0 的 support 是 16，这意味着测试集中实际属于类别 0 的样本数是 16。
# accuracy 是 0.86，这意味着模型在所有测试样本中的正确率是 86%。
# macro avg 是所有类别指标的算术平均值。
# weighted avg 是所有类别指标的加权平均值，其中权重为各个类别的支持数。


# 实验结果1
#               precision    recall  f1-score   support

#            0       0.75      0.75      0.75         4
#            1       0.80      0.80      0.80         5

#     accuracy                           0.78         9
#    macro avg       0.78      0.78      0.78         9
# weighted avg       0.78      0.78      0.78         9