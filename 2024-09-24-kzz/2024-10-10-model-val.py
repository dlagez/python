import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# 加载保存的模型
model_path = '2024-09-24-kzz/model/model_20241010_170524.pkl'  # 请确保路径正确
model = joblib.load(model_path)

# 假设你有新的数据文件
new_data = pd.read_excel('data/2024-09-24-kzz/raw/BND_Cbdrpch-2022-sample.xlsx')  



# 选择与训练时相同的因子
X_new = new_data[['Liscd', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']]
print(X_new)
# 使用相同的标准化器进行数据预处理
scaler = StandardScaler()
X_new_scaled = scaler.fit_transform(X_new)  # 假设使用之前定义的 `scaler`
print('X_new_scaled', X_new_scaled)
# 进行预测
y_new_pred = model.predict(X_new_scaled)

# 打印预测结果
print("新数据的预测结果：")
print('y_new_pred',y_new_pred)

# 假设你有新数据的真实值
y_new_true = new_data['Clsprc']  # 请确保与之前的目标变量一致
print('y_new_true', y_new_true)

# 打印回归评价指标
def print_regression_metrics(y_true, y_pred, dataset_name):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)  # 计算均方根误差
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    print(f"{dataset_name} 评价指标：")
    print(f"均方误差 (MSE): {mse:.4f}")
    print(f"均方根误差 (RMSE): {rmse:.4f}")  # 打印 RMSE
    print(f"平均绝对误差 (MAE): {mae:.4f}")
    print(f"R^2 分数: {r2:.4f}")
    print("-" * 40)

# 计算并打印评价指标
print_regression_metrics(y_new_true, y_new_pred, "新数据集")




