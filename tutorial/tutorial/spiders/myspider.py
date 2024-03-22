import scrapy
import pandas as pd

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
                print("第一步：organization链接：" + link)
                # item = NAItem()
                # item['link'] = link
                # yield item

                # https://report.nih.gov/award/index.cfm?ot=&fy=2024&state=MA,NJ,NY&ic=&fm=&orgid=2705601&distr=&rfa=&om=n&pid=#tab5
            if link and title:
                org_id = link.split('(')[1].split(',')[0]
                new_link = f"https://report.nih.gov/award/index.cfm?ot=&fy=2024&state=MA,NJ,NY&ic=&fm=&orgid={org_id}&distr=&rfa=&om=n&pid=#tab5"
                # yield {'title': title, 'link': new_link}
                yield scrapy.Request(new_link, callback=self.parse_detail, meta={'title': title})

    def parse_detail(self, response):
        # 在新链接的回调函数中提取表格数据
        data_list = []
        for row in response.css('#print_page > div.content_int > div.content_area_full > div > div > div.search_result > div > div.tab_content.tab5 > table.res_cont tr'):
            # 提取每个tr第二个td里面的数据
            data = row.css('td:nth-child(2)::text').extract_first()
            print("第二步：提取的data数据：" + data)
            if data:
                data_list.append(data)
            # 检查是否有数据
        if data_list:
            # 提取链接和标题
            print("data_list" + data_list)
            link = response.css('a.tablelink::attr(href)').extract_first()
            print("第二步的link："+ link)
            title = response.css('a.tablelink::text').extract_first()
            if link and title:
                yield {'title': title, 'data_list': data_list, 'link': link}



        
        
