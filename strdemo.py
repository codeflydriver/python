#coding=utf-8
mystr="Hello world itcast and itcastcpp"
print mystr.find('itcast')
print mystr[12:]
print mystr.find('itcast',13)
print mystr[23:]
print len(mystr)
print mystr.index('itcast')
print mystr.count('itcast')
print type(mystr)
demostr=mystr.decode(encoding='utf-8')
print type(demostr)
demo2str=mystr.decode(encoding='utf-8',errors='strict')
print type(demo2str)
czstr=mystr.replace('itcast','传智播客')
print czstr
czstr=czstr.replace('传智播客','itcast')
print czstr
czstr=czstr.replace('itcast','传智播客',1)
print czstr
mylist=mystr.split( ' ')
print mylist
for key in mylist:
    print key
my2list=mystr.split(' ',2)
print my2list
mystr=mystr.replace('H','h',1)
print mystr.capitalize()
print mystr.center(50)
print mystr.endswith('itcastcpp')
print mystr.startswith('Hello')
print mystr.isalnum()
print mystr.isalpha()
