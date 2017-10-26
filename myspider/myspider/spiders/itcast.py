# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import scrapy
from myspider.items import ItcastItem

class MySpider(scrapy.Spider):
    # 爬虫名，启动爬虫的时候必须要的参数
    name = 'itcast'
    # url域，非必须可选参数。不是在这个域下面的地址将会被忽略
    allowed_domains = ['http://www.itcast.cn']
    # 要爬的网站地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list=response.xpath("//div[@class='li_txt']")
        # 创建一个列表用来保存所有的item信息
        items=[]
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item=ItcastItem()
            # .extract()将xpath对象转换为Unicode字符串
            # xpath()返回的是一个列表
            name=node.xpath("./h3/text()").extract()
            title=node.xpath("./h4/text()").extract()
            info=node.xpath("./p/text()").extract()
            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]
            items.append(item)
        return items