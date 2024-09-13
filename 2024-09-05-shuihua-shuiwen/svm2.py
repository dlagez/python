import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.decomposition import PCA
import joblib
import os

# 加载模型
# 检查文件是否存在
if not os.path.exists('model/mlp_model.pkl'):
    print("File does not exist.")
else:
    try:
        # 加载模型
        loaded_svm_model = joblib.load('model/mlp_model.pkl')
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading the model: {e}")

# 定义特征列名
columns = ['氨氮', 'COD', '总磷', '气温', '相对湿度', '降雨量', '风速', '光照时长']

# 自己构造假数据
# 一行就是一天的数据。
data = [
    [1.571, 24.433, 0.159, 5.5, 60, 0.0, 7, 11.12],
    [1.571, 4, 6, 5.5, 60, 0.0, 7, 11.12],
    [6, 24.433, 0.159, 6, 60, 0.0, 7, 13],
    [0.49,	67.91,	0.14,	24.5,	90,	0,	3,	14.12]
]

# 创建DataFrame
df = pd.DataFrame(data, columns=columns)


# 使用加载的模型进行预测
y_pred_loaded = loaded_svm_model.predict(df)

print(y_pred_loaded)


