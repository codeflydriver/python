# -*- coding: utf-8 -*-
import scrapy
from tencenthr.items import TencenthrItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseURL="http://hr.tencent.com/position.php?&start="
    offset=0
    start_urls = [baseURL+str(offset)]


    def parse(self, response):
        node_list=response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item=TencenthrItem()
            item['positionName']=node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
            item['positionLink']=node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")
            if len(node.xpath("./td[2]/text()")):
                item['positionType']=node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            else:
                item['positionType']=""
            item['peopleNumber']=node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            item['workLocation']=node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            item['publishTime']=node.xpath("./td[5]/text()").extract()[0].encode("utf-8")
            yield item
        # 直接获取下一页按钮的链接
        if len(response.xpath("//a[@class='noactive' and @id='next']"))==0:
            url=response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request("http://hr.tencent.com/"+url,callback=self.parse)
        # 在面对没有下一页按钮等情况的时候
        # if(self.offset<2350):
        #     self.offset+=10
        #     url=self.baseURL+str(self.offset)
        #     yield scrapy.Request(url,callback=self.parse)
# 自己定义一个回调方法
#     def parse_next(self,response):
#     pass
# //a[@id='next']/@href
#
