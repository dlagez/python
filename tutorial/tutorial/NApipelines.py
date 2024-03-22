# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class TutorialPipeline:
    def __init__(self):
        self.links = []

    def process_item(self, item, spider):
        self.links.append(item['link'])
        return item
    
    def close_spider(self, spider):
        df = pd.DataFrame({'Link': self.links})
        df.to_excel('links.xlsx', index=False)
