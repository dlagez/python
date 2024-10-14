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
from sklearn.linear_model import LinearRegression

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


model = LinearRegression()

model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_scaled)
trddt = df['Trddt']
results = pd.DataFrame({
    'Trddt': trddt,
    'y_pred': y_pred,
    'y': y
})



# 通过 Trddt 分组并计算每组的 MSE
mse_per_day = results.groupby('Trddt').apply(lambda x: mean_squared_error(x['y'], x['y_pred']))
# 将结果转换为 DataFrame，方便查看和保存
mse_per_day_df = mse_per_day.reset_index()
mse_per_day_df.columns = ['Trddt', 'MSE']  # 重命名列
output_path = 'predictions_with_trddt-line.xlsx'
mse_per_day_df.to_excel(output_path, index=False) 

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
print_regression_metrics(y, y_pred, "aa")
