# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class ExcelPipeline:
    def __init__(self):
        self.result_data = []

    def process_item(self, item, spider):
        self.result_data.append(item)
        return item

    def close_spider(self, spider):
        # 在Spider关闭时保存数据到Excel文件
        df = pd.DataFrame(self.result_data)
        df.to_excel('output.xlsx', index=False)

