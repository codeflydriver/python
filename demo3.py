# coding=utf-8
for letter in 'Python':
    print 'current letter:',letter
fruits=['banana','apple','mango']
for fruit in fruits:
    print "current fruit:",fruit
    if fruit=='apple':
        break
else:
    print "fruit was ate"
demolist=[1,2,3,4]
print "这是列表：",demolist
print "这是列表第一位：",demolist[0]
demolist.pop(3)
print "删减后的列表",demolist
demolist.append(5)
print "append后的列表",demolist
del demolist[0]
print "删除后的列表",demolist
print "列表取值：",demolist[0]
demolist[0]=8
print "列表改变值",demolist
demolist.append('hello world')
print "追加一个helloworld",demolist
demolist.append([1,2,3])
print "追加一个数组",demolist
print "列表拼接",demolist+[100,200]
print "列表长度",len(demolist)
demolist=demolist*2
print "列表乘以二:",demolist
print "判断列表中有无元素200",200 in demolist
print "判断列表中有无元素hello world",'hello world' in demolist
print "取列表前五个元素",demolist[0:3]
demolist2=demolist[0:5]
print "比较两个列表",cmp(demolist,demolist2)
demolist.sort()
print "排序后的列表",demolist
