import pymysql
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib
from tensorflow.keras.models import load_model
from datetime import datetime

# 代码有问题，抛弃这个文件，留存。


# 设置打印选项
np.set_printoptions(precision=3, suppress=True)

# 连接到数据库
def get_db_connection():
    return pymysql.connect(
        host='localhost',   # 数据库地址
        user='root',        # 用户名
        password='password',# 密码
        database='water_quality_db' # 数据库名
    )

# 从数据库读取数据
def load_data_from_db():
    connection = get_db_connection()
    query = "SELECT temperature, humidity, rainfall, wind_speed, sunshine_duration FROM water_quality"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# 将预测结果写入数据库
def save_predictions_to_db(predictions, svm_predictions):
    connection = get_db_connection()
    cursor = connection.cursor()

    current_date = datetime.now().strftime('%Y-%m-%d')
    insert_query = """
        INSERT INTO water_quality (date, temperature, humidity, rainfall, wind_speed, sunshine_duration, result)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for i in range(len(predictions)):
        cursor.execute(insert_query, (
            current_date, 
            predictions[i][0], 
            predictions[i][1], 
            predictions[i][2], 
            predictions[i][3], 
            predictions[i][4], 
            1 if svm_predictions[i] == '有' else 0  # 水华结果
        ))
    connection.commit()
    connection.close()

# 加载数据
df = load_data_from_db()

# 提取特征
data = df[['temperature', 'humidity', 'rainfall', 'wind_speed', 'sunshine_duration']].values

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
model = load_model('2024-09-05-水华项目-水文/model/lstm_relu_model_20240905_103037.keras')

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
svm_model_path = '2024-09-05-水华项目-水文/model/mlp_model_best.pkl'
if not os.path.exists(svm_model_path):
    print("SVM model file does not exist.")
else:
    try:
        loaded_svm_model = joblib.load(svm_model_path)
        svm_predictions = loaded_svm_model.predict(prediction_df)
        
        svm_predictions_str = ['无' if pred == 0 else '有' for pred in svm_predictions]
        prediction_df['result'] = svm_predictions_str
        
        # 将预测结果保存到数据库
        save_predictions_to_db(prediction_df.values, svm_predictions_str)

        # 打印结果
        print(prediction_df)

    except Exception as e:
        print(f"Error loading the SVM model: {e}")
