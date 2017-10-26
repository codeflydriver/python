#coding=utf-8
class Employee:
    '''
    this is a demo class
    '''
    classstr="it is a test class"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def hello(self):
        '''
        say hello 
        '''
        print self.name
        print "say hello"
class Parent:   #定义父类
    parentAttr=100
    def __init__(self):
        print "调用父类构造函数"
    def parentMethod(self):
        print "调用父类方法"
    def setAttr(self,attr):
        Parent.parentAttr=attr
        print "父类属性：",Parent.parentAttr
    def getAttr(self):
        print "父类属性：",Parent.parentAttr
    def sayHello(self):
        print "Hello chuanzhiboke"
class child(Parent):    #定义子类
    def __init__(self):
        Parent()
        print "调用子类的构造方法"
    def childMethod(self):
        print "调用子类方法：child method"
    def sayHello(self):
        print "Hello itcast"