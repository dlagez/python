import scrapy
import pandas as pd
import json

class MySpider(scrapy.Spider):
    name = 'myspider2'
    start_urls = ['https://reporter.nih.gov/services/Projects/ProjectInfo?projectId=11010073']
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # 解析 JSON 响应
        data = json.loads(response.body)

        # 提取 abstract_text 字段的值
        abstract_text = data.get('abstract_text')

        if abstract_text:
            print("提取的 abstract_text 数据是：" + abstract_text)
        else:
            print("没有提取到 abstract_text 数据")
       
        