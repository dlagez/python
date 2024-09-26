import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


# 使用债券代码、'Sperchge', 'Cnvtvalu', 'Cvtprmrt'四个因子进行训练
# 使用增强模型


# 加载数据
df = pd.read_excel('data/2024-09-24-kzz/result/processed_data_20240924_152213.xlsx')

# 选择因子与目标变量
X = df[['Liscd', 'Sperchge', 'Cnvtvalu', 'Cvtprmrt']]
y = df['Clsprc']  # 假设你要预测 Opnprc

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 数据划分
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 定义要搜索的参数范围
param_grid = {
    'n_estimators': [100, 200, 300],  # 决策树数量
    'max_depth': [None, 10, 20, 30],  # 最大深度
    'min_samples_split': [2, 5, 10],  # 最小样本分割数
    'min_samples_leaf': [1, 2, 4],    # 最小叶节点样本数
    'max_features': ['auto', 'sqrt']   # 特征数量
}

model = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, 
                           scoring='neg_mean_squared_error', cv=3, 
                           verbose=2, n_jobs=-1)
grid_search.fit(X_train, y_train)

train_score = grid_search.score(X_train, y_train)
val_score = grid_search.score(X_val, y_val)
test_score = grid_search.score(X_test, y_test)
print(f'Train Score: {train_score}, Validation Score: {val_score}, Test Score: {test_score}')

# 输出最佳参数和最佳得分
print("最佳参数:", grid_search.best_params_)
print("最佳得分:", -grid_search.best_score_)
