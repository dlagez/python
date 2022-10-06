from datetime import date
from operator import concat
import requests
import parsel   #解析源代码
import csv
from asyncore import write
import json
import pandas as pd

index_ = ['日期','最高温度','最低温度', '天气','风向']  # 选取的气象要素
dataSum = pd.DataFrame(columns=index_)  # 建立一个空dataframe
for year in range(2012,2019):
    for month in range(1,13):
        url = f'https://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D=57083&areaInfo%5BareaType%5D=2&date%5Byear%5D={year}&date%5Bmonth%5D={month}'
        response = requests.get(url)
        #print(response)
        json_data = response.json()
        #print(json_data['data'])
        a = json_data['data']
        select1 = parsel.Selector(a)
        trs = select1.css('table tr') 
        date,dtemp,gtemp,con,wind = [],[],[],[],[]
        for tr in trs[1:]:
            tds = tr.css('td::text').getall()
            print(tds)
            date.append(tds[0])
            gtemp.append(''.join(tds[1:2]))
            dtemp.append(''.join(tds[2:3]))
            con.append(''.join(tds[3:4]))
            wind.append(''.join(tds[4:5]))
        data = pd.DataFrame()
        data['日期'] = date
        data['最高温度'] = gtemp
        data['最低温度'] = dtemp
        data['天气'] = con
        data['风向'] = wind
        dataSum = pd.concat(dataSum, data, axis=0)
print(dataSum)
# data.to_excel('天气.xlsx')
               
            
