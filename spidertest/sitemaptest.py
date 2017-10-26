#coding=utf-8
import re
from wswptest import download
def crawl_sitemap(url):
    #下载网站地图文件
    sitemap=download(url)
    # 提取网站地图连接
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    # 下载这些链接
    for link in links:
        html=download(link)