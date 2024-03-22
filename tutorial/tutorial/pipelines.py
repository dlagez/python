# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:
    def process_item(self, item, spider):
        return item

import pandas as pd

class ExcelPipeline:
    def __init__(self):
        self.result_data = []

    def process_item(self, item, spider):
        self.result_data.append(item)
        return item

    def close_spider(self, spider):
        if self.result_data:
            titles = []
            data_lists = []
            links = []
            for item in self.result_data:
                titles.append(item['title'])
                data_lists.append(item['data_list'])
                links.append(item['link'])
            
            df = pd.DataFrame({
                'Title': titles,
                'Data List': data_lists,
                'Link': links
            })
            df.to_excel('output.xlsx', index=False)
