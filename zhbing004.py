# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

# import os
# print('Process (%s) start...' % os.getpid())
#
# pid=os.fork()   #Windows没有fork调用
# if pid==0:
#     print('我是子进程(%s),我的父进程是%s' % (os.getpid(),os.getppid()))
# else:
#     print('我(%s)创建了一个子进程(%s)' % (os.getpid(),pid))

#########################################################################################################
from multiprocessing import Process
import os

def run_proc(name):
    print('运行子进程%s(%s)...' % (name,os.getpid()))   #子进程执行代码

if __name__=='__main__':
    print('父进程%s' % os.getpid())
    p=Process(target=run_proc,args=('test',))   #创建子进程:传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    print('子进程将启动')
    p.start()
    p.join()   #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('子进程结束')
#########################################################################################################

















