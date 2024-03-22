import scrapy
import pandas as pd

class MySpider(scrapy.Spider):
    name = 'myspider2'
    start_urls = ['https://reporter.nih.gov/project-details/10825897']
    def parse(self, response):
        data = response.css('#abstract_text > div > div::text').get()
        if data:
            print("提取的数据是：" + data)
        else:
            print("没有提取到数据")
        