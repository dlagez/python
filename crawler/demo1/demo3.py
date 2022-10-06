import requests
import re
import pandas as pd
# import seaborn as sns
import warnings
# import matplotlib.pyplot as plt

#设置为seaborn风格
# sns.set()
#不显示警告
warnings.filterwarnings("ignore")
# plt.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#正则表达式提取数据
r1 = '<td>(.*?)</td>'
re1 = re.compile(r1)
r2 = '<td style="color:#ff5040;">(.*?)</td>'
re2 = re.compile(r2)
r3 = '<td style="color:#3097fd;" >(.*?)</td>'
re3 = re.compile(r3)

#浏览器headers
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5'}

#爬取天气链接的地址
url = 'http://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D=59131&areaInfo%5BareaType%5D=2&date%5Byear%5D=2021&date%5Bmonth%5D=6'
#requests访问网页源码
df = requests.get(url,headers = headers).json()['data']
#正则表达式提取日期
date = [l.split(' ')[0] for l in re1.findall(df)[::4]]
#正则表达式提取星期
week = [l.split(' ')[1] for l in re1.findall(df)[::4]]
#正则表达式提取最高温度
wd_h = re2.findall(df)
#正则表达式提取最低温度
wd_w = re3.findall(df)
#正则表达式提取天气情况
wea = re1.findall(df)[1::4]
#正则表达式提取风力
win = re1.findall(df)[2::4]

#创建dataframe存储数据
datas = pd.DataFrame()
datas['日期'] = pd.to_datetime(date)
datas['星期'] = week
datas['最高气温'] = wd_h
datas['最低气温'] = wd_w
datas['天气情况'] = wea
datas['风力'] = win
datas.to_excel('data.xlsx',index = None)