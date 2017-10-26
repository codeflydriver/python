import requests
res=requests.get("http://www.itcast.cn")
savefile=open("itcast.html","w")
savefile.write(res.content)

savefile.close()