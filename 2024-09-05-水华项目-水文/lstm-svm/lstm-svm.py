import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import load_model
from datetime import datetime


# 读取lstm模型，并使用模型预测数据。

# 设置打印选项：精度为3位小数，禁用科学计数法
np.set_printoptions(precision=3, suppress=True)

# 假设数据已经加载到DataFrame中
df = pd.read_csv('data/sh/Book1.csv')

# 提取相关特征（假设已经有数据）
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
# 加载模型
model = load_model('2024-09-05-水华项目-水文/model/lstm_relu_model_20240905_103037.keras')

# 预测未来7天的数据
last_14_days = X_test[-1]  # 使用测试集最后14天的数据来预测未来7天
prediction = model.predict(np.array([last_14_days]))

# 将预测结果转换为原始形状和反归一化
prediction = prediction.reshape((7, Y.shape[2]))  # 7天，每天有多个特征
prediction = scaler.inverse_transform(prediction)

# 创建一个DataFrame来保存预测结果
prediction_df = pd.DataFrame(prediction, columns=['气温', '相对湿度', '降雨量', '风速', '光照时长'])
prediction_df = prediction_df.round(3)

# 获取当前时间，格式为 YYYYMMDD_HHMMSS
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')

# 保存预测结果到一个新的CSV文件
prediction_filename = f'2024-09-05-水华项目-水文/result/prediction_results_{current_time}.csv'
prediction_df.to_csv(prediction_filename, index=False)

# 打印预测结果
print(prediction)   


# 加载SVM模型
svm_model_path = '2024-09-05-水华项目-水文/model/mlp_model_best.pkl'
if not os.path.exists(svm_model_path):
    print("SVM model file does not exist.")
else:
    try:
        # 加载SVM模型
        loaded_svm_model = joblib.load(svm_model_path)
        print("SVM model loaded successfully.")
        
        # 使用SVM模型进行预测
        svm_predictions = loaded_svm_model.predict(prediction_df)
        
        # 将预测结果拼接到DataFrame中
        # prediction_df['是否有水华'] = svm_predictions

        # 将 0 和 1 转换为 "无" 和 "有"
        svm_predictions_str = ['无' if pred == 0 else '有' for pred in svm_predictions]

        # 将转换后的预测结果拼接到DataFrame中
        prediction_df['是否有水华'] = svm_predictions_str
        
        # 保存最终结果到CSV文件
        # 生成文件名并保存预测结果
        prediction_filename = f'2024-09-05-水华项目-水文/result/prediction_results_lstm_bp_{current_time}.csv'
        prediction_df.to_csv(prediction_filename, index=False)
        
        # 打印最终结果
        print(prediction_df)
        
    except Exception as e:
        print(f"Error loading the SVM model: {e}")