import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# 使用债券代码、'Sperchge', 'Cnvtvalu', 'Cvtprmrt'四个因子进行训练
# 使用普通模型

# 加载数据
df = pd.read_excel('data/2024-09-24-kzz/result/processed_data_20240924_152213.xlsx')

# 选择因子与目标变量
X = df[['Liscd', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']]
y = df['Clsprc']  # 假设你要预测 Opnprc

df['Trddt'] = pd.to_datetime(df['Trddt'])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 数据划分
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 定义要搜索的参数范围


model = LinearRegression()

model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_test)


# 取前100个数据
y_test_sample = y_test[:100]
y_pred_sample = y_pred[:100]

# 绘制实际值与预测值的对比图
plt.figure(figsize=(10, 6))

# 绘制真实值
plt.plot(y_test_sample.values, label='Actual Values', color='blue', marker='o')

# 绘制预测值
plt.plot(y_pred_sample, label='Predicted Values', color='red', marker='x')

plt.title('Actual vs Predicted Values (First 100 Samples)')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


