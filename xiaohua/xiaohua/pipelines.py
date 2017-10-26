# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from xiaohua.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class XiaohuaPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link=item['imageLink']
        print image_link
        scrapy.Request(image_link)
    
