from sklearn.linear_model import LinearRegression
import numpy as np

# 生成一些示例数据
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

X
y
# 创建并训练线性回归模型
model = LinearRegression().fit(X, y)


# 预测
predictions = model.predict(np.array([[3, 5]]))
print(predictions)