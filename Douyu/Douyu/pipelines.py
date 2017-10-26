# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link=item['imageLink']
        print image_link
        yield scrapy.Request(image_link)
    def item_completed(self, results, item, info):
        image_path=[x["path"] for ok,x in results if ok]
        os.rename(IMAGES_STORE+image_path[0],IMAGES_STORE+item["nickName"]+".jpg")
        return item
    # def process_item(self, item, spider):
    #     return item
