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
def triangle_yang():
    L=[1]
    while True:
        yield L
        L=[L[x]+L[x+1] for x in range(len(L)-1)]
        L=[1]+L+[1]

n=0
for i in triangle_yang():
    print(i)
    n=n+1
    if n==10:
        break
####################################################
print([x*x for x in range(20)])

























