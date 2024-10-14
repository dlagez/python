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

new_data['Trddt'] = pd.to_datetime(new_data['Trddt'])
# new_data = new_data.sort_values(by='Trddt')

# 选择与训练时相同的因子
X_new = new_data[['Liscd', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']]



# 使用相同的标准化器进行数据预处理
X_new_scaler1 = scaler1.transform(X_new)
# X_new_scaler2 = scaler2.transform(X_new)

# 进行预测
y_pred_1 = model_1.predict(X_new_scaler1)
y_pred_2 = model_2.predict(X_new_scaler1)

# 假设你有新数据的真实值
y_true = new_data['Clsprc']
trddt = new_data['Trddt']  # 确保你有 Trddt 列

results = pd.DataFrame({
    'Trddt': trddt,
    'y_true': y_true,
    'y_pred_1': y_pred_1,
    'y_pred_2': y_pred_2
})


# 根据日期对数据进行分组，并计算每天的 MAE
mae_per_day_1 = results.groupby('Trddt').apply(lambda x: mean_absolute_error(x['y_true'], x['y_pred_1']))
mae_per_day_2 = results.groupby('Trddt').apply(lambda x: mean_absolute_error(x['y_true'], x['y_pred_2']))



# 将结果保存为 Excel 文件
# output_path = 'mae_per_day_model_1.xlsx'
# results.to_excel(output_path, index=False)  # 不保存索引


# 创建折线图
plt.figure(figsize=(10, 6))
plt.plot(mae_per_day_1.index, mae_per_day_1.values, label='RandomForest MAE')
plt.plot(mae_per_day_2.index, mae_per_day_2.values, label='LinearRegression MAE', linestyle='--')

# 设置图表标题和标签
plt.title('MAE per Day for Two Models')
plt.xlabel('Date')
plt.ylabel('MAE')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# 显示图表
plt.show()