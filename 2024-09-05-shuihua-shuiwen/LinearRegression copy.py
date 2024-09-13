import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 生成示例时间序列数据
dates = pd.date_range('2023-01-01', periods=100)
data = np.random.randn(100).cumsum()
time_series = pd.Series(data, index=dates)
dates
data
time_series


# 创建特征和标签
time_series = time_series.reset_index()
time_series.columns = ['Date', 'Value']
time_series['Day'] = time_series['Date'].dt.day
time_series['Month'] = time_series['Date'].dt.month
time_series['Year'] = time_series['Date'].dt.year

# 使用前90天的数据训练模型，后10天的数据作为测试
train = time_series[:-10]
test = time_series[-10:]

train
test

# 特征和标签
features = train[['Day', 'Month', 'Year']]
labels = train['Value']

features
labels

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(features, labels)

# 预测未来10天的数据
future_dates = pd.date_range('2023-04-11', periods=10)
future_data = pd.DataFrame({'Date': future_dates})
future_data['Day'] = future_data['Date'].dt.day
future_data['Month'] = future_data['Date'].dt.month
future_data['Year'] = future_data['Date'].dt.year

future_features = future_data[['Day', 'Month', 'Year']]
future_predictions = model.predict(future_features)

future_features
future_predictions

# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(time_series['Date'], time_series['Value'], label='Observed')
plt.plot(future_data['Date'], future_predictions, label='Forecast')
plt.legend()
plt.show()
