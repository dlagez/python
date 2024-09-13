import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib
from tensorflow.keras.models import load_model
from datetime import datetime
import sys
import json
from pathlib import Path


# 代码有问题，抛弃这个文件，留存。

json_data = sys.argv[1]

print("Received JSON data:", json_data)  # 打印接收到的 JSON 数据
data = json.loads(json_data)

print("data:", data)

# 将JSON数据转换为DataFrame
df = pd.DataFrame(data)

# 提取相关特征
feature_columns = ['temperature', 'humidity', 'rainfall', 'windSpeed', 'sunshineDuration']
data_values = df[feature_columns].values

# 在这里进行数据处理或使用LSTM模型进行预测
# model = load_lstm_model()  # 假设模型加载的函数
# predictions = model.predict(data_values)

print("数据处理完成：")
print(data_values)

# 提取特征
data = df[['temperature', 'humidity', 'rainfall', 'windSpeed', 'sunshineDuration']].values

# 数据归一化
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# 创建输入序列和输出目标
def create_dataset(data, time_step=1, future_days=7):
    X, Y = [], []
    for i in range(len(data)-time_step-future_days):
        X.append(data[i:(i+time_step), :])
        Y.append(data[(i+time_step):(i+time_step+future_days), :])
    return np.array(X), np.array(Y)

time_step = 14
X, Y = create_dataset(scaled_data, time_step, future_days=7)

# 划分训练集和测试集
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
Y_train, Y_test = Y[:train_size], Y[train_size:]

# 加载LSTM模型
model_path = Path('D:/code/python/2024-09-05-shuihua-shuiwen/model/lstm_relu_model_20240905_103037.keras')
model = load_model(model_path)

# 预测未来7天的数据
last_14_days = X_test[-1]  # 使用测试集最后14天的数据来预测未来7天
prediction = model.predict(np.array([last_14_days]))

# 反归一化预测结果
prediction = prediction.reshape((7, Y.shape[2]))
prediction = scaler.inverse_transform(prediction)

# 将预测结果转为DataFrame
prediction_df = pd.DataFrame(prediction, columns=['temperature', 'humidity', 'rainfall', 'wind_speed', 'sunshine_duration'])
prediction_df = prediction_df.round(3)

# 加载SVM模型并预测水华状况
# svm_model_path = 'D:\code\python\2024-09-05-shuihua-shuiwen\model\mlp_model_best.pkl'
svm_model_path = Path('D:\code\python\2024-09-05-shuihua-shuiwen\model\mlp_model_best.pkl')
if not os.path.exists(svm_model_path):
    print("SVM model file does not exist.")
else:
    try:
        loaded_svm_model = joblib.load(svm_model_path)
        svm_predictions = loaded_svm_model.predict(prediction_df)
        
        prediction_df['result'] = svm_predictions
        result_json = prediction_df.to_json(orient='records')
        # 打印结果
        print(result_json)

    except Exception as e:
        print(f"Error loading the SVM model: {e}")
