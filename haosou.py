#coding=utf-8
import requests
myparams={'q':'linux'}
r=requests.get('https://www.haosou.com/s',params=myparams)
print r.url
print '⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐'
print r.content
fp=open('linux.html','w')
fp.write(r.content)
fp.close()