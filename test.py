# coding=utf-8
def printname(parameter):
    #    "print your name by str"
    print parameter
    return


# coding=utf-8
def changeme(parameter):
    parameter.append([1, 2, 3, 4])
    print "函数内取值：", parameter
    return
# coding=utf-8
def changeto100(x):
    x=100
    return
#encoding=utf-8
def changeyou(a,b):
    print a
    return
#coding=utf-8
def changeshe(a=1,b=5):
    print 'a=%d' % a
    print 'b=%d' % b
    return
def arglist(**a):
    print a
    for key in a:
        print key+'='+str(a[key])
    return
