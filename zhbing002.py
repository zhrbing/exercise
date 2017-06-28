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


class GrandFather():
    def run_Grand(self):
        print('GrandFather run...')

class Father(GrandFather):
    def run_father(self):
        print('Father run...')

class son(Father):
    pass

testson=son()
testson.run_father()
testson.run_Grand()




















