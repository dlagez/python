import scrapy
from .. import NAItem 

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://report.nih.gov/award/index.cfm?ot=&fy=2024&state=MA,NJ,NY&ic=&fm=&orgid=&distr=&rfa=&om=n&pid=&view=statedetail']

    def parse(self, response):
        # 在这里解析页面内容
        # 使用XPath定位表格
        table = response.xpath('//*[@id="orgtable"]')
        # 提取表格数据
        
        for row in table.xpath('.//tr'):
            # 提取第一列单元格的链接
            link = row.xpath('.//td[1]/a/@href').extract_first()
            title = row.xpath('.//td[1]/a/text()').extract_first()
            if link:
                print("提取的链接：" + link)
                # item = NAItem()
                # item['link'] = link
                # yield item

                # https://report.nih.gov/award/index.cfm?ot=&fy=2024&state=MA,NJ,NY&ic=&fm=&orgid=2705601&distr=&rfa=&om=n&pid=#tab5
            if link and title:
                org_id = link.split('(')[1].split(',')[0]
                new_link = f"https://report.nih.gov/award/index.cfm?ot=&fy=2024&state=MA,NJ,NY&ic=&fm=&orgid={org_id}&distr=&rfa=&om=n&pid=#tab5"
                yield {'title': title, 'link': new_link}

        
        
