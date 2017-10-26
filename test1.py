#coding=utf-8
import test
test.printname('张正')
mylist=[10,20,30,40]
test.changeme(mylist)
print "函数外取值：",mylist
var=200
test.changeto100(var)
print var
test.changeyou(1,2)
test.changeyou(b=1,a=20)
test.changeshe()
test.arglist(x=12,y=24,z=48)