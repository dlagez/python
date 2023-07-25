# read file data/erbu.xlsx use pandas
import pandas as pd
df = pd.read_excel('data/erbu.xlsx')
df['year'] = df['Reptdt'].str[:4].astype(int)
df['weight'] = df.groupby(['Stkcd', 'PersonID'])['year'].transform(lambda x: x - x.min() + 1)
df.head(10)
df.to_excel('data/erbu_weight.xlsx', index=False)