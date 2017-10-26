#coding=utf-8
demodict={'aa':123,'bb':456}
print demodict
print demodict['aa']
for key in demodict:
    print key,demodict[key]
del demodict['aa']
print demodict
print "My name is %s and I am %d" % ('ery',20)