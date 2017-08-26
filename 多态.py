__author__ = 'Administrator'


class SchoolMember(object):
   def __init__(self,name,age,cource):
       self.name = name
       self.age = age
       self.cource = cource

class Teacher(SchoolMember):
    def __init__(self):
        pass

class Student(SchoolMember):
    def __init__(self,name,age):
        super(Student,self).__init__(name,age)



'''
   多态的作用是 实现接口的重用


'''

class Animal(object):
    def __init__(self,name):
        self.name = name
        pass

    def talk(self):
        pass

    def animal_talk(self,language):
        print(language)



class Cat(Animal):
    def __init__(self,name):
        super(Cat,self).__init__(name)

class Dog(Animal):
    '''
     这个类的描述信息
    '''
    def __getitem__(self,item):
        print("getitem")

    def __setitem__(self, key, value):
        print("setitem",key,value)
        #self[key]=value


    def __delitem__(self, key):
        pass

    def __init__(self,name):
        super(Dog,self).__init__(name)


    def  __call__(self, *args, **kwargs):
        print("runnning call",args,kwargs)


    def __str__(self):
       return "<obj:%s>" %self.name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)


c = Cat("徐两位")

d = Dog("chenronghua")


d["dsfdsf"]="gaochao"

d.defdfd ="gaochao"


d(1,3,3,4,5,name=3)

'''
hasattr()
setattr()
getattr()
delattr()

  计算机之间通信 两根线之前通信 可以传递的图片 视频 文本
  所以我们 先说 大家知道网络通信的话 我可以传视频 传网页
  不同类型是可以通过不同的协议来支持的
  smtp
  http
  dns
  ftp
  ssh
  snmp 简单的网络监控的
  icmp ping包
  dhcp 做ip地址分配的
  ...
  这些协议来来回回也是数据的交换  脸上之后传数据流 我们的工作方式不一样
  怎么工作 但是 无论如何变换都离不开数据的交换 本质上来讲
  我们对于这种数据交换可以总结为 两种方式 发 收
  send receive 本质上面 所有的协议都是基于发和收
  首先说 网络有一个7层模型 osi7层模型 应用层
  数据 a 和 b想 实现通信 必须遵循一些规格
  tcp/ip(三次握手 四次断开)  udp

  应用层
  表示层
  会话层
  传输层
  网络层  tcp  认识ip 就是说 上面有一些限制要求的  必须要满足一些什么条件
  数据链路层   不认识mac地址 只认识mac
  物理层
'''





















print("Dog--__dict__",Dog.__dict__)

print("d--__dict__:",d.__dict__)

print(d)

c.animal_talk("woof")

d.animal_talk("miaomiao")


'''
 class Dog(object):

 __moudle__表示当前操作的对象在那个模块

 __class__当前操作的对象属于哪个类 类是什么

'''

def func(self):
    print("func")

Foo = type("Foo",(object,),{"func":func})

f = Foo()
f.func()
