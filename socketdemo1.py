#coding=utf-8
from socket import *
myhost=''
myport=12345
sockobj=socket(AF_INET,SOCK_STREAM)#AF_INET表示ipv4协议，SOCK_STREAM表示tcp流式传输
sockobj.bind((myhost,myport))
sockobj.listen(128)
while True:
    connection,address=sockobj.accept()
    print "connect by:",address
    while True:
        data=connection.recv(1024)
        if not data:
            break
        connection.send('echo:'+data)
        connection.close()
