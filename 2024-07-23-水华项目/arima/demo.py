import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# 假设你的数据已经读取到一个DataFrame中
data = pd.read_csv('data/sh/data.csv', sep='\t')  # 将数据替换为你的实际数据路径

# 选择一个你希望预测的特征作为目标变量，比如"是否有蓝藻"
y = data['是否有蓝藻']

# 拟合ARIMA模型
model = ARIMA(y, order=(5, 1, 0))  # 参数order需要根据数据的ACF/PACF图来确定
model_fit = model.fit()

# 预测未来7天
forecast = model_fit.forecast(steps=7)
print(forecast)
