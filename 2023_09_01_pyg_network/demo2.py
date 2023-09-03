import numpy as np

# 创建两个示例的二维 NumPy 数组
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6]])

# 在垂直方向合并数组
merged_array = np.vstack((array1, array2))

# 打印合并后的数组
print("垂直合并后的数组：")
print(merged_array)


import numpy as np

# 创建两个示例的 NumPy 数组
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# 使用 numpy.hstack() 水平合并两个数组
merged_array = np.hstack((array1, array2))

# 打印合并后的数组
print("水平合并后的数组：")
print(merged_array)