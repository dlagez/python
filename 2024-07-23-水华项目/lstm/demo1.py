import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 假设数据已经加载到DataFrame中
df = pd.read_csv('data/sh/Book1.csv')

# 提取相关特征（假设已经有数据）
data = df[['氨氮(mg/L)', 'COD(mg/L)', '总磷(mg/L)', '气温（℃）', '相对湿度（%）', '降雨量（mm）', '风速（km/h）', '光照时长（h）']].values

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

time_step = 14  # 使用过去14天的数据来预测未来7天
X, Y = create_dataset(scaled_data, time_step, future_days=7)

# 将数据划分为训练集和测试集
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
Y_train, Y_test = Y[:train_size], Y[train_size:]

# 构建LSTM模型
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_step, X.shape[2])))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(Y.shape[1] * Y.shape[2]))  # 预测未来7天，每天都有多个特征

model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
model.fit(X_train, Y_train.reshape(Y_train.shape[0], -1), epochs=20, batch_size=1)

# 预测未来7天的数据
last_14_days = X_test[-1]  # 使用测试集最后14天的数据来预测未来7天
prediction = model.predict(np.array([last_14_days]))

# 将预测结果转换为原始形状和反归一化
prediction = prediction.reshape((7, Y.shape[2]))  # 7天，每天有多个特征
prediction = scaler.inverse_transform(prediction)

# 打印预测结果
print(prediction)