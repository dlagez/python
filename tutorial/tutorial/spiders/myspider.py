import scrapy
import pandas as pd
import re
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

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
                org_id = link.split('(')[1].split(',')[0].strip("'")
                new_link = f"https://report.nih.gov/award/index.cfm?ot=&fy=2024&state=MA,NJ,NY&ic=&fm=&orgid={org_id}&distr=&rfa=&om=n&pid=#tab5"
                print("第一步：data页面链接是：" + new_link)
                # yield {'title': title, 'link': new_link}
                num = num + 1
                # if (num>3):
                #     break
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
            text = row.css('td:nth-child(2) a::text').get()
            # 提取第二个td中链接的地址
            link = row.css('td:nth-child(2) a::attr(href)').get()
            print("第二步：文本信息:", text)
            print("第二步：链接:", link)
            if link:
                # https://reporter.nih.gov/project-details/11010073#details
                # https://reporter.nih.gov/services/Projects/ProjectInfo?projectId=11010073
                js_link = self.convert_link(link)
                print("第二步：请求的js数据链接是：" + js_link)
                meta_data = {'original_link': link, 'project': text, 'data_url': response.url}
                if link:
                    yield scrapy.Request(js_link, callback=self.parse_detail2, meta=meta_data)

    def convert_link(self, original_link):
        # 使用正则表达式从链接中提取 projectId
        match = re.search(r'/project-details/(\d+)', original_link)
        if match:
            project_id = match.group(1)
            new_link = f'https://reporter.nih.gov/services/Projects/ProjectInfo?projectId={project_id}'
            return new_link
        else:
            return None
        
    def parse_detail2(self, response):
        # 解析 JSON 响应
        data = json.loads(response.body)
        # 提取链接
        link = response.request.url
        print("第三步：访问的链接是：" + link)
        # 提取 abstract_text 字段的值
        abstract_text = data.get('abstract_text')
        if abstract_text:
            print("第三步：提取的 abstract_text 数据是：" + abstract_text)
        else:
            print("第三步：没有提取到 abstract_text 数据")

        # 创建一个包含数据和链接的字典
        orgin_link = response.meta['original_link']
        print("第三步：文章链接：" + orgin_link)

        project = response.meta['project']
        print("第三步：原始项目名：" + project)

        data_url = response.meta['data_url']
        print("第三步：原始项目链接是：" + data_url)
        result = {
            'abstract_text': abstract_text,
            'link': link,
            'orgin_link':orgin_link,
            'project': project,
            'data_url': data_url
        }
        yield result

    




        
        
