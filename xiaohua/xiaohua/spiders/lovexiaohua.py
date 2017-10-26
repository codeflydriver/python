# -*- coding: utf-8 -*-
import scrapy
from xiaohua.items import XiaohuaItem


class LovexiaohuaSpider(scrapy.Spider):
    name = 'lovexiaohua'
    allowed_domains = ['www.xiaohuar.com']
    baseUrl="http://www.xiaohuar.com/list-1-"
    offset=0
    start_urls = [baseUrl+str(offset)+".html"]

    def parse(self, response):
        info_list=response.xpath("//div[@class='item masonry_brick masonry-brick']/div[@class='item_t']")
        for info in info_list:
            item=XiaohuaItem()
            item['xiaohuaName']=info.xpath("./div[@class='img']/a[@target='_blank']/img[1]/@alt").extract()[0].encode("utf-8")
            item['imageLink']=info.xpath("./div[@class='img']/a[@target='_blank']/img[1]/@src").extract()[0].encode("utf-8")
            yield item
        self.offset+=1
        yield scrapy.Request(self.baseUrl+str(self.offset)+".html",self.parse)
