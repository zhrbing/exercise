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
class Myc(object):
    pass

print(type(123))
print(type('abc'))
print(type(abs))
print(Myc())





