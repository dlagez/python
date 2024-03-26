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
        matched_keywords = self.contains_keywords(item)
        item['matched_keywords'] = matched_keywords
        if matched_keywords:
            self.result_data.append(item)
        return item

    def close_spider(self, spider):
        # 设置 Pandas 显示选项
        pd.set_option('display.max_colwidth', None)

        # 将数据转换为DataFrame并保存为Excel文件
        df = pd.DataFrame(self.result_data)
        df.to_excel('output4.xlsx', index=False)

    def contains_keywords(self, item):
        # 定义关键字列表
        keywords = ['omic', 'genomic', 'transcriptomic', 'epigenomic', 'single-cell', 'metagenomics', 'microbiome', 'cancer', 'tumor', 'RNA-seq', 'DNA', 'RNA', 'genom*', 'epigen*']
        matched_keywords = []
        # 检查关键字是否在文本中
        for keyword in keywords:
            if keyword.lower() in item['abstract_text'].lower():
                matched_keywords.append(keyword)
        return matched_keywords if matched_keywords else None
