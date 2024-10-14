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


def plot_prediction_vs_true(y_true, y_pred, dataset_name):
    plt.figure(figsize=(10, 6))
    
    plt.scatter(y_true, y_pred, color='blue', edgecolors='k', alpha=0.7, label="Predictions")
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2, label="True values")
    
    plt.xlabel("True Values")
    plt.ylabel("Predicted Values")
    plt.title(f"{dataset_name} - True vs Predicted Values")
    plt.legend()
    plt.grid(True)
    
    plt.show()


# 进行绘图
y_val_pred = model.predict(X_val)
plot_prediction_vs_true(y_val, y_val_pred, "验证集")

# (tensorflow) D:\code\python>C:/Users/admin/miniconda3/envs/tensorflow/python.exe d:/code/python/2024-09-24-kzz/2024-10-09-model-line.py  
# Train Score: 0.95225105717875, Validation Score: 0.9511208028193258, Test Score: 0.9541490708504397
# 测试集 评价指标：
# 均方误差 (MSE): 140.3249  
# 均方根误差 (RMSE): 11.8459
# 平均绝对误差 (MAE): 5.7352
# R^2 分数: 0.9541
# ----------------------------------------
# 验证集 评价指标：
# 均方误差 (MSE): 144.8285
# 均方根误差 (RMSE): 12.0345
# 平均绝对误差 (MAE): 5.7786
# R^2 分数: 0.9511
# ----------------------------------------
