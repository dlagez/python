import requests
import re
import json
from bs4 import BeautifulSoup
import pandas as pd

months = [1,2,3,4,5,6,7,8,9,10,11,12]
# years = [2015,2016,2017,2018,2019,2020,] 
years = [2020,] 
citys = []
citys = {54511: '北京', 57036: '西安', 56778: '昆明'}

# 2015 之前没有空气质量指数
index_ = ['日期','最高温','最低温', '天气','风力风向', '空气质量指数']  # 选取的气象要素
data = pd.DataFrame(columns=index_)  # 建立一个空dataframe

for city in citys:
	for y in years:
		for m in months:
			# url = 'http://tianqi.2345.com/Pc/GetHistory?areaInfo[areaId]=349727&areaInfo[areaType]=1&date[year]='+str(y)+'&date[month]='+str(m)
			url = 'http://tianqi.2345.com/Pc/GetHistory?areaInfo[areaId]='+str(city)+'&areaInfo[areaType]=2&date[year]='+str(y)+'&date[month]='+str(m)
			print(url)
			response = requests.get(url=url)
			if response.status_code == 200:  # 防止url请求无响应
				#print(json.loads(response.text)['data'])
				html_str = json.loads(response.text)['data']
				soup = BeautifulSoup(html_str,'lxml')
				tr = soup.table.select("tr")
				for i in tr[2:]:
					td = i.select('td')
					tmp = []
					for j in td:
						#print(re.sub('<.*?>',"",str(j)))
						tmp.append(re.sub('<.*?>',"",str(j)))
					#print(tmp)
					data_spider = pd.DataFrame(tmp).T
					data_spider.columns = index_  # 修改列名
					# data_spider.index = date  # 修改索引
					# data_spider = data_spider.set_axis(data_spider.iloc[0], axis=1, inplace=False)  # 修改索引
					data = pd.concat((data,data_spider), axis=0)  # 数据拼接
	# print(data.iloc[:1], )
	# data = data.set_axis(data.iloc[1], axis=1, inplace=False)
	print(data)
	data.to_excel('weatherdata_ny-'+str(citys[city])+'.xlsx')