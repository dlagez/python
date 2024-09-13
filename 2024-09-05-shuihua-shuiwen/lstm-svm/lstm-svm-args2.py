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

json_data = sys.argv[1]

# print("Received JSON data:", json_data)  # 打印接收到的 JSON 数据
data = json.loads(json_data)

# print("data:", data)

# 将JSON数据转换为DataFrame
df = pd.DataFrame(data)

# 提取相关特征
feature_columns = ['temperature', 'humidity', 'rainfall', 'windSpeed', 'sunshineDuration']
data_values = df[feature_columns].values

# 在这里进行数据处理或使用LSTM模型进行预测
# model = load_lstm_model()  # 假设模型加载的函数
# predictions = model.predict(data_values)

# print("数据处理完成：")
# print(data_values)


# 数据归一化
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data_values)

# print('scaled_data: ', scaled_data)



# 加载LSTM模型
model_path = Path('D:/code/python/2024-09-05-shuihua-shuiwen/model/lstm_relu_model_20240905_103037.keras')
model = load_model(model_path)

# 预测未来7天的数据
prediction = model.predict(np.array([scaled_data]))

# 反归一化预测结果
prediction = prediction.reshape((7, data_values.shape[1]))
prediction = scaler.inverse_transform(prediction)


# 将预测结果转为DataFrame
prediction_df = pd.DataFrame(prediction, columns=['气温', '相对湿度', '降雨量', '风速', '光照时长'])
prediction_df = prediction_df.round(3)

# print('预测的结果为：', prediction_df)

# 加载SVM模型并预测水华状况
# svm_model_path = 'D:\code\python\2024-09-05-shuihua-shuiwen\model\mlp_model_best.pkl'
svm_model_path = Path(r'D:\code\python\2024-09-05-shuihua-shuiwen\model\mlp_model_best.pkl')
if not os.path.exists(svm_model_path):
    print("SVM model file does not exist.")
else:
    try:
        loaded_svm_model = joblib.load(svm_model_path)
        svm_predictions = loaded_svm_model.predict(prediction_df)

        # print('svm 预测结果为：', svm_predictions)
        
        prediction_df['result'] = svm_predictions

        feature_columns = ['temperature', 'humidity', 'rainfall', 'windSpeed', 'sunshineDuration', 'result']
        # 将 DataFrame 的列名从中文转换为英文
        prediction_df.columns = feature_columns

        result_json = prediction_df.to_json(orient='records')
        # 打印结果
        print(result_json)
        sys.stdout.flush()

    except Exception as e:
        print(f"Error loading the SVM model: {e}")
