import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import load_model


# 读取lstm模型，并使用模型预测数据。

# 设置打印选项：精度为3位小数，禁用科学计数法
np.set_printoptions(precision=3, suppress=True)

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
# 加载模型
model = load_model('data/sh/model/lstm_relu_model.keras')

# 预测未来7天的数据
last_14_days = X_test[-1]  # 使用测试集最后14天的数据来预测未来7天
prediction = model.predict(np.array([last_14_days]))

# 将预测结果转换为原始形状和反归一化
prediction = prediction.reshape((7, Y.shape[2]))  # 7天，每天有多个特征
prediction = scaler.inverse_transform(prediction)

# 创建一个DataFrame来保存预测结果
prediction_df = pd.DataFrame(prediction, columns=['氨氮(mg/L)', 'COD(mg/L)', '总磷(mg/L)', '气温（℃）', '相对湿度（%）', '降雨量（mm）', '风速（km/h）', '光照时长（h）'])
prediction_df = prediction_df.round(3)

# 保存预测结果到一个新的CSV文件
prediction_df.to_csv('data/sh/result/prediction_results.csv', index=False)

# 打印预测结果
print(prediction)
