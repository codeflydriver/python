#coding=utf-8
import requests
dest_url="https://book.douban.com/subject_search?search_text=python&cat=1001"
res=requests.get(url=dest_url)
print res