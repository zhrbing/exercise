# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

#面向对象编程
# class Student(object):
#
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#
#     def print_score(self):
#         print('%s:%s' % (self.name,self.score))
#
#     def print_grade(self):
#         if self.score>=90:
#             print('A')
#         elif self.score>=60:
#             print('B')
#         else:
#             print('C')
#
# bart=Student('Bart Simpson',59)
# bart.print_score()
# bart.print_grade()

#多态
# class Animals(object):
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animals):
#     def run(self):
#         print('Dog is running...')
#
# class Cat(Animals):
#     def run(self):
#         print('Cat is running...')
#
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Dog())
# run_twice(Cat())
#
# class Tortoise(Animals):
#     def run(self):
#         print('Tortoise is running slowly...')
#
# run_twice(Tortoise())

###########################################################################
# #定义一个父类和一个子类
# class Province(object):
#     def __init__(self,proname):
#         self.proname=proname
#
#     def ps(self):
#         print('I am in %s.' % self.proname)
#
# class City(Province):
#     def __init__(self,proname,cityname):
#         self.cityname=cityname
#         Province.__init__(self,proname)
#
#     def ps1(self):
#         print('I am in %s-%s.' % (self.proname,self.cityname))
#
# #定义一个独立的类
# class Timer(object):
#     def ps(self):
#         print('我不属于Province类或其子类，但我有ps方法我同样可以被调用')
#
#     def ps1(self):
#         print('我不属于Province类或其子类，但我有ps方法我同样可以被调用')
#
# #定义一个函数
# def f(x):
#     x.ps()
#     x.ps1()
#
# f(City('上海','浦东'))
# f(Timer())
###########################################################################
#判断对象类型
# class Myc(object):
#     pass
#
# print(type(123))
# print(type('abc'))
# print(type(abs))
# print(Myc())
# print(type(None))
#
# #type()函数返回类型--对应的Class类型
# print(type(123)==int)

# import types
# def f():
#     pass
#
# print(type(f)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print((type(lambda x:x)==types.LambdaType))
# print(type((x for x in range(10)))==types.GeneratorType)

# print(isinstance(b'a',bytes))
# print(isinstance([1,2,3],(list,tuple)))#判断变量是否某类型中的一种
###########################################################################
# print(dir('abc'))#以list形式返回一个对象的所有属性和方法
#
# class MyObject(object):
#     def __init__(self):
#         self.x=9
#
#     def power(self):
#         return self.x*self.x
#
# obj=MyObject()
# print(hasattr(obj,'x'))
# print(obj.x)
# print(hasattr(obj,'y'))
# setattr(obj,'y',10)
# print(hasattr(obj,'y'))
# print(getattr(obj,'y'),obj.y)
#
# print(getattr(obj,'z',404))
#
# print(hasattr(obj,'power'))
# print(getattr(obj,'power'))
# fn=getattr(obj,'power')
# print(fn)
# print(fn())
###########################################################################
#给实例绑定属性：通过实例变量，或通过self变量
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#
# s=Student('Bob')
# s.score=90   #通过类创建的实例可以任意绑定属性
# print(s.name,s.score)

# class Student(object):
#     name='Student'   #定义类属性
#
# s=Student()
# print(s.name)  #创建实例后获取实例属性，实例没有name属性，会获取类的name属性
# print(Student.name)   #获取类的name属性
#
# s.name='Michael'  #给实例绑定name属性
# print(s.name)   #获取实例的name属性，会覆盖类的name属性
# print(Student.name)   #类的name属性不变
#
# del s.name
# print(s.name)   #删除实例的name属性后，调用s.name会获取类的name属性
###########################################################################
# class Student(object):
#     pass
#
# s=Student()
# s.name='Michael'    #给实例动态绑定属性
# print(s.name)
#
# def set_age(self,age):
#     self.age=age
#
# from types import MethodType
# s.set_age=MethodType(set_age,s)     #给实例动态绑定方法
# s.set_age(25)
# print(s.age)
#
# s2=Student()
# # s2.setage(25)       #对别的实例不起作用
#
# def set_score(self,score):
#     self.score=score
#
# Student.set_score=set_score   #给类绑定方法，所有实例均可调用
#
# s.set_score(100)
# s2.set_score(90)
# print(s.score,s2.score)
###########################################################################
# class Student(object):
#     __slots__ = ('name','age')  #限制绑定属性
#
# s=Student()
# s.name='Michael'
# s.age=25
# # s.score=90  #score未在slots添加，无法绑定
#
# class GraduateStudent(Student):
#     pass
#
# g=GraduateStudent()
# g.name='Bob'
# g.age=27
# g.score=100     #__slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用，即子类不受其限制
# print(g.name,g.age,g.score)
###########################################################################
# class Student(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value<0 or value>100:
#             raise ValueError('score must between 0~100')
#         self._score=value
#
# s=Student()
# s.set_score(60)
# print(s.get_score())
# s.set_score(9999)

#@property装饰器:把一个方法变成属性调用
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value<0 or value>100:
#             raise ValueError('score must between 0~100')
#         self._score=value
#
# s=Student()
# s.score=60
# print(s.score)
# s.score=99999

#只读属性:只定义getter方法，不定义setter方法
# class Student(object):
#
#     @property
#     def birth(self):
#         return self.birth
#
#     @birth.setter       #birth可读写属性
#     def birth(self,value):
#         self._birth=value
#
#     @property
#     def age(self):     #age只读属性
#         return 2017-self._birth
#
# s=Student()
# s.birth=1990
# print(s.age)


# class GrandFather():
#     def run_Grand(self):
#         print('GrandFather run...')
#
# class Father(GrandFather):
#     def run_father(self):
#         print('Father run...')
#
# class son(Father):
#     pass
#
# testson=son()
# testson.run_father()
# testson.run_Grand()

################################################

# list_arr=[8,2,1,0,3]
# list_index=[2,0,3,2,4,0,1,3,2,3,3]
# list_tel=''
# for i in list_index:
#     list_tel+=str(list_arr[i])
#
# print(list_tel)

################################################
#__str__
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#
#     def __str__(self):
#         return 'Student object(name:%s)' % self.name
#
#     __repr__=__str__
#
# stu=Student('Mike')
# print(stu)
################################################
#__iter__
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>10000:
#             raise StopIteration()
#         return self.a
#
# for n in Fib():
#     print(n)
################################################
#getitem
# class Fib(object):
#     def __getitem__(self, item):
#         a,b=1,1
#         for x in range(item):
#             a,b=b,a+b
#         return a
#
# print(Fib()[100])
# for x in range(20):
#     print('Fib('+str(x+1)+')=',Fib()[x])

# class Fib(object):
#     def __getitem__(self, item):
#         if isinstance(item,int):     #item是索引
#             a,b=1,1
#             for x in range(item):
#                 a,b=b,a+b
#             return a
#         if isinstance(item,slice):    #item是切片
#             start=item.start
#             stop=item.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
#
# print(Fib()[10])
# print(Fib()[:10])
################################################
#__getattr__
# class Chain(object):
#     def __init__(self,path=''):
#         self._path=path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path,path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__=__str__
#
# print(Chain().status.user.timeline.list)
################################################
#定义__call__()方法，直接对实例进行调用:把对象看成函数
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
# Student('Mike')()
#
# #callable()：判断一个对象是否“可调用”
# print(callable(Student('')))
# print(callable(max))
# print(callable('str'))
################################################
#使用枚举类
# from enum import Enum
# Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__members__.items():
#     print(name,'——>',member,',',member.value)
#
# from enum import Enum,unique
# @unique    #保证没有重复值
# class Weekday(Enum):
#     Sun=0
#     Mon=1
#     Tue=2
#     Wed=3
#     Thu=4
#     Fri=5
#     Sat=6
#
# print(Weekday.Thu.value)
# print(Weekday(1))
# for name,member in Weekday.__members__.items():
#     print(name,'——>',member,'——>',member.value)
################################################
# from hello import Hello
# h=Hello()
# h.hello()
# print(type(Hello))
# print(type(h))
# print(type(123))
# print(type([1,2]))
################################################
#错误处理
# try:
#     print('try...')
#     r=10/int(input('Input a interger:'))
#     print('result:',r)
# except ValueError as e:
#     print('Value:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# else:     #没有错误发生时，自动执行
#     print('No error!')
# finally:
#     print('finally...')
# print('end...')


#logging模块记录错误信息，让程序继续执行
# import logging
# def foo(s):
#     return 10/int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('end...')

#调试
# import logging
# logging.basicConfig(level=logging.INFO)
# n=0
# logging.info('n=%d' % n)
# print(10/n)

#单元测试
# class Dict(dict):          #被测试的类：行为和dict一致，但可以通过属性访问
#     def __init__(self,**kw):
#         super().__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key]=value
#
# import unittest
# class TestDict(unittest.TestCase):    #测试类：从unittest.TestCase继承
#     def test_init(self):              #以test开头的方法是测试方法，不以test开头的方法测试时不会执行
#         d=Dict(a=1,b='test')
#         self.assertEqual(d.a,1)       #断言判断
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,dict))
#
#     def test_key(self):
#         d=Dict()
#         d['key']='value'
#         self.assertEqual(d.key,'value')
#
#     def test_attr(self):
#         d=Dict()
#         d.key='value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'],'value')
#
#     def test_keyerror(self):
#         d=Dict()
#         with self.assertRaises(KeyError):
#             value=d['empty']
#
#     def test_attrerror(self):
#         d=Dict()
#         with self.assertRaises(AttributeError):
#             value=d.empty
#
#     def setUp(self):            #setUp()和tearDown()分别在每调用一个测试方法的前后被执行
#         print('Test start<<<')
#
#     def tearDown(self):
#         print('             >>>Test end')
#
# if __name__=='__main__':
#     unittest.main()
#
# d=Dict(a=1,b='test')
# print(d['a'])
# print(d.b)
################################################
#文件读写
# with open('/home/zhbing/桌面/000','r') as f:     #与try ... finally是一样的，但代码更简洁，且不必调用f.close()方法
#     print(f.read())             #read()一次性读取文件全部内容
#     print(f.read(10))            #read(size)每次最多读取size个字节的内容
#     print(f.readline())             #readline()每次读取一行
#     print(f.readlines())            #readlines()一次性读取所有内容并按行返回list
#     for line in f.readlines():
#         print(line.strip())     #去掉末尾的\n

# with open('/home/zhbing/桌面/111','w') as f:
#     f.write('Hello world.\n\nhello')
################################################











