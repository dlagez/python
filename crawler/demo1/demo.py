from cgitb import html
from email import contentmanager
import encodings
import gzip
import requests
import pandas as pd
import re
import io

months = [1,2,3,4,5,6,7,8,9,10,11,12]
# years = [2015,2016,2017,2018] 
years = [2015] 
# citys = [54511,57036,56778] # 北京，西安，昆明
citys = [54511] # 北京，西安，昆明

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
}

index_ = ['MaxTemp','MinTemp', 'WindDir', 'Wind', 'Weather','Aqi','AqiInfo','AqiLevel']  # 选取的气象要素
data = pd.DataFrame(columns=index_)  # 建立一个空dataframe
for c in citys:
    for y in years:
        for m in months:
            # 找到json格式数据的url
            if (y<2017) or (y==2017)&(m<=11):
                url = "http://tianqi.2345.com/t/wea_history/js/"+str(c)+"_"+str(y)+str(m)+".js" # ?qq-pf-to=pcqq.c2c
            else:
                url = "http://tianqi.2345.com/t/wea_history/js/"+str(y)+str(m).zfill(2)+"/"+str(c)+"_"+str(y)+str(m).zfill(2)+".js"
            print(url)
            response = requests.get(url=url, headers=headers)
            # response.encoding = 'utf-8'
            response.encoding=response.apparent_encoding
            print(response.content)
            print('------------------------------------------------------------')
            print(response.text)                         
            if response.status_code == 200:  # 防止url请求无响应             
                response2 = response.text.replace("'", '"')  # 这一步可以忽略
                #  利用正则表达式获取各个气象要素（方法不唯一）
                date = re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", response2)[:-2]
                mintemp = re.findall('yWendu:"(.*?)℃', response2)
                maxtemp = re.findall('bWendu:"(.*?)℃', response2)
                winddir = re.findall('fengxiang:"([\u4E00-\u9FA5]+)',response2)
                wind = re.findall('fengli:"([\u4E00-\u9FA5]+)',response2)
                weather = re.findall('tianqi:"([[\u4E00-\u9FA5]+)~?', response2)
                aqi = re.findall('aqi:"(\d*)',response2)
                aqiInfo = re.findall('aqiInfo:"([\u4E00-\u9FA5]+)',response2)
                aqiLevel = re.findall('aqiLevel:"(\d*)',response2)
                data_spider = pd.DataFrame([maxtemp,mintemp, winddir, wind, weather,aqi,aqiInfo,aqiLevel]).T
                data_spider.columns = index_  # 修改列名
                data_spider.index = date  # 修改索引
                data = pd.concat((data,data_spider), axis=0)  # 数据拼接
                print('%s年%s月的数据抓取成功' % (y, m))
            else:
                print('%s年%s月的数据不存在' % (y, m))
                break
data.to_excel('weatherdata.xlsx')
print('爬取数据展示：\n', data)