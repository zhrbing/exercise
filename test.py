# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

# for i in range(9):
#     for j in range(9):
#         if (i + 1 >= j + 1):
#             print(str(i + 1) + "*" + str(j + 1) + "=" + str((i + 1) * (j + 1)), end="\t")
#     print()


# msg1='张冰'.encode('utf-8')
# msg2=b'\xe5\xbc\xa0\xe5\x86\xb0'.decode('utf-8')
#
# print(msg1,'字节数',len(msg1))
# print(msg2,'字符数',len(msg2))

# num=355/113
# print('%.2f' % num)

# print('%02d%%-%04d-%06d' % (11,222,3333))

# s1=72
# s2=85
# r=(s2-s1)/s1*100
# print('小明的成绩提高了%.1f%%' % r)

# for i in range(3,12,2):
#     print(i)

# squares = [3,2,1,0,1, 4, 9, 16, 25]
# squares2=[36,49,64,81,100]
# print(squares)
# print(squares[0])
# print(squares[-1])
# print(squares[-3])
# print(squares[-3:])
# print(squares[:])
# print(squares+squares2)
# squares.insert(0,121)
# print(squares)
# squares.remove(1)
# print(squares)
# squares.pop()
# print(squares)
# squares.pop(0)
# print(squares)
# squares.insert(2,1)
# print(squares)
# print(squares.index(1,3,len(squares)))
# print(squares.count(1))
# squares.sort()
# print(squares)
# squares.reverse()
# print(squares)

# squares3=[]
# for i in range(10):
#     squares3.append(i**2)
# print(squares3)

# squares4 = [x ** 3 for x in range(10)]
# print(squares4)
#
# squares5=[(x,y) for x in[1,2,3] for y in [3,1,4] if x!=y]
# print(squares5)

# from math import pi
# squares6=[str(round(pi,i)) for i in range(6)]
# print(squares6)

# matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix2=[[row[i] for row in matrix] for i in range(4)]
# print(matrix2)

# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

# print(list(zip(*matrix)))

# t=(1,2,[3,4])
# t[2][0]=5
# t[2][1]=6
# print(t)

# sum=0
# for x in range(101):
#     sum=sum+x
# print(sum)

# sum=0
# x=1
# while x<101:
#    sum=sum+x
#    x=x+1
# print(sum)

# l=['Bart','Lisa','Adam']
# for name in l:
#     print("Hello,",name)

# dd={1:'甲',2:'乙',4:'丁',3:'丙'}
# print(dd)
# dd[5]='戊'
# print(dd)
# dd['a']='己'
# print(dd)
# del dd['a']
# print(dd)
# print(list(dd.keys()),'\n',sorted(dd.keys()))
# print(1 in dd)

# dd={x:x**3 for x in range(5)}
# print(dd)
#
# dd2=dict(a=1,b=4,c=9,d=16)
# print(dd2)

# ss=set([1,3,4,2,4,5])
# print(ss)

# s1=set([1,2,3])
# s2=set([2,3,4])
# print(s1&s2,'\n',s1|s2)

# a='abc'
# print(a.replace('a','A'))
# print(a)

# def abs_my(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('错误的参数。。。')
#     if x>=0:
#         return x
#     if x<0:
#         return -x
#
# print(abs_my('a'))

import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# print('%.2f\t%.2f' % move(100, 100, 60, math.pi / 6))

# def sqrtmy(a,b,c):
#     x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
#     x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
#     return x1,x2
# print('%.2f\t%.2f' % sqrtmy(1,3,-4))

# def power(x,n):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
#
# print(power(5,3))

# def add_end(l=[]):
#     l.append('END')
#     return l
#
# print(add_end([1,2,3]))
# print(add_end([4,5,6]))
# print(add_end())
# # 默认参数已改变
# print(add_end())


# def cal00(*nums):
#     sum=0
#     for x in nums:
#         sum=sum+x
#     return sum
#
# print(cal00(1,2))
# print(cal00(1,2,3))
# print(cal00(1,2,3,4))
#
# nums00=[1,2,3,4,5]
# print(cal00(*nums00))

# def person(name,age,**kw):
#     print('name:',name,'age:',age,'OTHERS:',kw)
#
# person('zhrbing',30)
# person('zhrbing',30,city='shanghai')
# person('zhrbing',30,city='Beijing',gender='M')
#
# def person00(name,age,*,city,job):
#     print(name,age,city,job)
#
# person00('zhrbing',30,city='shanghai',job='writer')

# def f1(a,b,c=0,*args,**kw):
#     print(a,b,c,args,kw)

# f1(1,2)
# f1(1,2,3)
# f1(1,2,3,'a','b')
# f1(1,2,3,'a','b',x=4,y=5)
# f1(1,2,z=6)
# args=(11,22,33)
# kws={'d':44,'e':55,'f':66}
# f1(*args,**kws)

# def fact(n):
#     if n<0:
#         print('请输入正整数:')
#     elif (n==1 or n==0):
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(0))
# print(fact(3))
# print(fact(4))
# print(fact(5))
# print(fact(-10))
# print(fact(10))
# print(fact(1000))

# def fib(n):
#     a,b=1,1
#     num=1
#     while a<n:
#         print('%10d' % a, end='\t')
#         a,b=b,a+b
#         if num % 5 ==0:
#             print()
#         num=num+1
#
# fib(100000)

# def ask_ok(prompt,retries=4,reminder="Please try again!"):
#     while True:
#         ok=input(prompt)
#         if ok in('y','Y','yes','YES'):
#             return True
#         if ok in('n','no','N','NO'):
#             return False
#         retries=retries-1
#         if retries<0:
#             raise ValueError('invalid user')
#         print(reminder)
#
# ask_ok('Do you really want to quit?')

# i=5
# def f(arg=i):
#     print(arg)
#
# i=6
# f()

# l=list(range(100))
# print(l[1:11])
# print(l[-10:])
# print(l[::10])
#
# t=tuple(range(100))
# print(t[:5])
#
# print('abcdefg'[:3])

# d={1:'a',2:'b',3:'c',4:'d'}
# for k in d:
#     print(k,end='\t')
# print()
# for v in d.values():
#     print(v,end='\t')
# print()
# for k0,v0 in d.items():
#     print(k0,v0,end=', ')

# for ch in '123':
#     print(ch,end=',')

# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance((4,5,6),Iterable))
# print(isinstance({1:'a',2:'b',3:'c'},Iterable))

# l=['a','b','c','d']
# for k,v in enumerate(l):
#     print(k,v,end=', ')

# for i,j,k in [(1,2,3),(4,5,6),(7,8,9)]:
#     print(i,j,k)

# print(list(range(1,11)))
# print([x*x for x in range(1,11) if x%2==0])
# print([x+y for x in 'ABC' for y in 'def'])

# l=['Hello','World',18,'Apple',None]
# l0=[]
# for lv in l:
#     if isinstance(lv,str):
#         l0.append(lv.upper())
# print(l0)

print([x.upper() for x in ['Hello',16,'World',18,'Apple',None] if isinstance(x,str)])
























