import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 加载两个模型
model_path_1 = '2024-09-24-kzz/model/model_LinearRegression_20241014_145640.pkl'  # 模型 1
model_path_2 = '2024-09-24-kzz/model/model_RandomForestRegressor_20241014_145450.pkl'  # 模型 2 (假设另一个模型路径)
model_1 = joblib.load(model_path_1)
model_2 = joblib.load(model_path_2)

# 加载新的数据
new_data = pd.read_excel('data/2024-09-24-kzz/raw/BND_Cbdrpch.xlsx')

# 筛选 Liscd 为 110031 的数据
new_data = new_data[new_data['Liscd'] == 113548]

new_data['Trddt'] = pd.to_datetime(new_data['Trddt'])
new_data = new_data.sort_values(by='Trddt')

# 选择与训练时相同的因子
X_new = new_data[['Liscd', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']]



# 使用相同的标准化器进行数据预处理
scaler = StandardScaler()
X_new_scaled = scaler.fit_transform(X_new)

# 进行预测
y_pred_1 = model_1.predict(X_new_scaled)
y_pred_2 = model_2.predict(X_new_scaled)

# 假设你有新数据的真实值
y_true = new_data['Clsprc']
trddt = new_data['Trddt']  # 确保你有 Trddt 列

# 绘制折线图进行对比
plt.figure(figsize=(15, 6))
plt.plot(trddt, y_true, label='True Values', color='black', linestyle='-', marker='o', markersize=4)
plt.plot(trddt, y_pred_1, label='Model 1 Predictions', color='blue', linestyle='--', marker='x', markersize=4)
plt.plot(trddt, y_pred_2, label='Model 2 Predictions', color='green', linestyle='-.', marker='s', markersize=4)

plt.title('True Values vs Model Predictions over Time')
plt.xlabel('Trddt')
plt.ylabel('Clsprc')
plt.xticks(rotation=45)  # 旋转 x 轴标签以避免重叠
plt.legend()
plt.grid(True)
plt.tight_layout()  # 调整图形以避免标签重叠
plt.show()
