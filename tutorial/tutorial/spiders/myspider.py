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
        
        num = 0

        for row in table.xpath('.//tr'):
            # 提取第一列单元格的链接
            link = row.xpath('.//td[1]/a/@href').extract_first()
            title = row.xpath('.//td[1]/a/text()').extract_first()
            if link and title:
                print("第一步：organization链接：" + link)
                org_id = link.split('(')[1].split(',')[0]
                new_link = f"https://report.nih.gov/award/index.cfm?ot=&fy=2024&state=MA,NJ,NY&ic=&fm=&orgid={org_id}&distr=&rfa=&om=n&pid=#tab5"
                print("第一步：data页面链接是：" + new_link)
                # yield {'title': title, 'link': new_link}
                num = num + 1
                if (num>3):
                    break
                yield scrapy.Request(new_link, callback=self.parse_detail, meta={'title': title})

    def parse_detail(self, response):
        # 在新链接的回调函数中提取表格数据
        # 循环十次或直到页面中没有更多行为止
        table = response.css('#print_page > div.content_int > div.content_area_full > div > div > div.search_result > div > div.tab_content.tab5 > table.res_cont')
        if not table:
            print("table 没有找到！")
            return
        rows = table.css('tr')
        if not rows:
            print("rows 没有找到！")
            return
        for row in rows:
            # 提取第二个td的文本信息
            text = row.css('td:nth-child(2)::text').get()
            # 提取第二个td中链接的地址
            link = row.css('td:nth-child(2) a::attr(href)').get()
            print("第二步：文本信息:", text)
            print("第二步：链接:", link)
            if link:
                yield scrapy.Request(link, callback=self.parse_detail2)
    
    def parse_detail2(self, response):
        data = response.xpath('//*[@id="abstract_text"]/div/div/text()').extract_first()
        if data:
            print("页面的数据是：" + data)
            # keywords = ['omic', 'genomic', 'transcriptomic', 'epigenomic', 'single-cell', 'metagenomics', 'microbiome', 'cancer', 'tumor', 'RNA-seq', 'DNA', 'RNA', 'genom*', 'epigen*']
            # for keyword in keywords:
            #     if keyword.lower() in data.lower():
            #         print(f"页面包含关键字 '{keyword}'，链接为：{response.url}")
            # yield {
            #     'link': response.url,
            #     'text': data
            # }




        
        
