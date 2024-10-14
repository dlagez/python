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

# 使用债券代码、'Sperchge', 'Cnvtvalu', 'Cvtprmrt'四个因子进行训练
# 使用普通模型

# 加载数据
df = pd.read_excel('data/2024-09-24-kzz/result/processed_data_20240924_152213.xlsx')

# 选择因子与目标变量
X = df[['Liscd', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']]
y = df['Clsprc']  # 假设你要预测 Opnprc

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 数据划分
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 定义要搜索的参数范围


model = RandomForestRegressor(random_state=42)

model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_test)

# 计算得分
train_score = model.score(X_train, y_train)
val_score = model.score(X_val, y_val)
test_score = model.score(X_test, y_test)
print(f'Train Score: {train_score}, Validation Score: {val_score}, Test Score: {test_score}')

# 打印回归评价指标
def print_regression_metrics(y_true, y_pred, dataset_name):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)  # 计算均方根误差
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # 计算 MAPE
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100  # 计算 MAPE

    print(f"{dataset_name} 评价指标：")
    print(f"均方误差 (MSE): {mse:.4f}")
    print(f"均方根误差 (RMSE): {rmse:.4f}")  # 打印 RMSE
    print(f"平均绝对误差 (MAE): {mae:.4f}")
    print(f"R^2 分数: {r2:.4f}")
    print(f"平均绝对百分比误差 (MAPE): {mape:.4f}%")  # 打印 MAPE
    print("-" * 40)


# 打印评价信息
# print_regression_metrics(y_train, model.predict(X_train), "训练集")
print_regression_metrics(y_test, y_pred, "测试集")
print_regression_metrics(y_val, model.predict(X_val), "验证集")


current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
joblib.dump(model, f'2024-09-24-kzz/model/model_RandomForestRegressor_{current_time}.pkl')
joblib.dump(scaler, f'2024-09-24-kzz/scaler/scaler_RandomForestRegressor_{current_time}.pkl')
