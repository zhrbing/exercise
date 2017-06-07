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

def fib(max):
    n, a, b = 1, 1, 1
    while n <= max:
        print('%3d' % a, end='\t')
        a, b = b, a + b
        n = n + 1

fib(8)