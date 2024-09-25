import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, ReLU
from datetime import datetime

# 2024-09-24全量水文数据，训练lstm模型

# 2024-09-05 训练lstm模型，并保存模型
# 设置打印选项：精度为3位小数，禁用科学计数法
np.set_printoptions(precision=3, suppress=True)

# 假设数据已经加载到DataFrame中
df = pd.read_excel('data/sh/2024-09-24-data/sw.xls')

# 提取相关特征（假设已经有数据）
df.columns = ['时间', '风速（km/h）', '降雨量（mm）', '相对湿度（%）', '气温（℃）', '光照时长（h）', '是否有水华']

# 选择所需的列
data = df[['气温（℃）', '相对湿度（%）', '降雨量（mm）', '风速（km/h）', '光照时长（h）']].values

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
model.add(ReLU())

model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
model.fit(X_train, Y_train.reshape(Y_train.shape[0], -1), epochs=20, batch_size=1)

current_time = datetime.now().strftime('%Y%m%d_%H%M%S')

model.save(f'2024-09-05-shuihua-shuiwen/model2/lstm_relu_model_{current_time}.keras')

# 预测未来7天的数据
last_14_days = X_test[-1]  # 使用测试集最后14天的数据来预测未来7天
prediction = model.predict(np.array([last_14_days]))

# 将预测结果转换为原始形状和反归一化
prediction = prediction.reshape((7, Y.shape[2]))  # 7天，每天有多个特征
prediction = scaler.inverse_transform(prediction)

# 创建一个DataFrame来保存预测结果
prediction_df = pd.DataFrame(prediction, columns=['气温（℃）', '相对湿度（%）', '降雨量（mm）', '风速（km/h）', '光照时长（h）'])

# 保存预测结果到一个新的CSV文件
prediction_df.to_csv(f'2024-09-05-shuihua-shuiwen/result/prediction_results_lstm_{current_time}.csv', index=False)

# 打印预测结果
print(prediction)