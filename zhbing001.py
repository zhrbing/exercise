# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

# l=[x*x for x in range(10)]
# print(l)

# 创建generator
# l0=(x*x for x in range(10))
# print(l0)
# print(next(l0))
# print(next(l0))
# for i in l0:
#     print(i,end='\t')

# def fib1(max):
#     n, a, b = 1, 1, 1
#     while n <= max:
#         print(a)
#         a, b = b, a + b
#         n = n + 1
# fib1(5)
#
# def fib2(max):
#     n, a, b = 1, 1, 1
#     while n <= max:
#         yield a
#         a, b = b, a + b
#         n = n + 1
# print(fib2(3))

#######################################################
# generator生成器实现杨辉三角
# def triangle_yang():
#     L=[1]
#     while True:
#         yield L
#         L=[L[x]+L[x+1] for x in range(len(L)-1)]
#         L=[1]+L+[1]
#
# n=0
# for i in triangle_yang():
#     print(i)
#     n=n+1
#     if n==10:
#         break
####################################################
# from collections import Iterable,Iterator
# print(isinstance([],Iterable))
# print(isinstance(100,Iterable))
#
# print(isinstance((),Iterator))
# print(isinstance(iter(()),Iterator))
# print(isinstance((x*x for x in range(10)),Iterator))

# def f00(x,y,f):
#     print(f(x)+f(y))
#
# f00(3,-6,abs)

# def f01(x):
#     return x*x
#
# v=map(f01,[1,2,3,4,5,6])
# print(list(v))

from functools import reduce
# def f02(x,y):
#     return 10*x+y
# print(reduce(f02,[1,3,5,7,9]))

# def str2int(s):
#     def f02(x,y):
#         return 10*x+y
#
#     def charm2num(s):
#         return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#
#     return reduce(f02,map(charm2num,s))
#
# print(str2int('111222333'))

# def is_odd(n):
#     return n%2==1
#
# l=list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
# print(l)

# l=[21,-10,35,-6,-77,9]
# print(sorted(l,key=abs))
#
# l0=['apple','Microsoft','google','IBM','Nokia']
# print(sorted(l0,key=str.lower,reverse=True))

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax+=n
        return ax
    return sum

f=lazy_sum(1,2,3,4,5)
print(f)
print(f())





