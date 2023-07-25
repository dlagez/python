# read file data/erbu.xlsx use pandas
import pandas as pd
df = pd.read_excel('data/erbu_2.xlsx')
df.head()
df.shape
type(df['year'][0])
df
df['year'] = df['Reptdt'].str[:4].astype(int)



group_muti = df.groupby(['Stkcd', 'PersonID'])
group_muti.head()
group_muti.indices
type(group_muti)
type(group_muti.indices)



group1 = group_muti.get_group((1, 301022))
group1.shape[0]
group1.reset_index()
type(group1)
type(group1.reset_index())
group1['index'] = group1.reset_index().index
group1['Reptdt'][396]
type(group1['Reptdt'][396])
type(group1['Reptdt'].loc[0])




group1['Reptdt'][396][:4]



for name, group in group_muti:
    print(name)
    print(group)
    





# df['weight'] = df.groupby(['Stkcd', 'PersonID']).index.transform(lambda x: x+1)
group_muti.head()
df['weight'] = df.groupby(['Stkcd', 'PersonID'])['year'].transform(lambda x: x - x.min() + 1)

df.head(20)



df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two'],
                   'C' : [1, 5, 5, 2, 5, 5],
                   'D' : [2.0, 5., 8., 1., 2., 9.]})
grouped = df.groupby('A')[['C', 'D']]
grouped.head()
list(grouped)