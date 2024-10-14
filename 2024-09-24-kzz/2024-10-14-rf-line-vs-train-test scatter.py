import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 加载两个模型
model_path_1 = '2024-09-24-kzz/model/model_RandomForestRegressor_20241014_152653.pkl'  # 模型 1
model_path_2 = '2024-09-24-kzz/model/model_LinearRegression_20241014_154200.pkl'  

scaler_path_1 = '2024-09-24-kzz/scaler/scaler_RandomForestRegressor_20241014_152653.pkl'  
scaler_path_2 = '2024-09-24-kzz/scaler/scaler_LinearRegression_20241014_154200.pkl'  

model_1 = joblib.load(model_path_1)
model_2 = joblib.load(model_path_2)
scaler1 = joblib.load(scaler_path_1)  # 加载保存的scaler
scaler2 = joblib.load(scaler_path_2)  # 加载保存的scaler

# 加载新的数据
new_data = pd.read_excel('data/2024-09-24-kzz/raw/BND_Cbdrpch.xlsx')

# 筛选 Liscd 为 113548 的数据
new_data = new_data[new_data['Liscd'] == 113548]

new_data['Trddt'] = pd.to_datetime(new_data['Trddt'])
new_data = new_data.sort_values(by='Trddt')

# 选择与训练时相同的因子
X_new = new_data[['Liscd', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']]

# 使用相同的标准化器进行数据预处理
X_new_scaler1 = scaler1.transform(X_new)
X_new_scaler2 = scaler2.transform(X_new)

# 进行预测
y_pred_1 = model_1.predict(X_new_scaler1)
y_pred_2 = model_2.predict(X_new_scaler2)

# 假设你有新数据的真实值
y_true = new_data['Clsprc']
trddt = new_data['Trddt']  # 确保你有 Trddt 列

# 创建标记数组，将 70% 数据标记为 1 类，30% 数据标记为 2 类
num_samples = len(new_data)
labels = np.zeros(num_samples)

# 随机选择 30% 的数据标记为 2 类
class_2_indices = np.random.choice(num_samples, size=int(num_samples * 0.3), replace=False)
labels[class_2_indices] = 2

# 剩下的数据标记为 1 类
labels[labels == 0] = 1

# 绘制折线图进行对比
plt.figure(figsize=(15, 6))

# 绘制类别为 1 的数据
plt.scatter(trddt[labels == 1], y_true[labels == 1], label='True Values (Class 1)', color='black', marker='o', s=50)
plt.scatter(trddt[labels == 1], y_pred_1[labels == 1], label='RandomForestRegressor Predictions (Class 1)', color='blue', marker='x', s=50)
plt.scatter(trddt[labels == 1], y_pred_2[labels == 1], label='LinearRegression Predictions (Class 1)', color='green', marker='s', s=50)

# 绘制类别为 2 的数据
plt.scatter(trddt[labels == 2], y_true[labels == 2], label='True Values (Class 2)', color='gray', marker='o', s=50)
plt.scatter(trddt[labels == 2], y_pred_1[labels == 2], label='RandomForestRegressor Predictions (Class 2)', color='cyan', marker='x', s=50)
plt.scatter(trddt[labels == 2], y_pred_2[labels == 2], label='LinearRegression Predictions (Class 2)', color='lime', marker='s', s=50)

plt.title('True Values vs Model Predictions over Time (Classified)')
plt.xlabel('Trddt')
plt.ylabel('Clsprc')
plt.xticks(rotation=45)  # 旋转 x 轴标签以避免重叠
plt.legend()
plt.grid(True)
plt.tight_layout()  # 调整图形以避免标签重叠
plt.show()
