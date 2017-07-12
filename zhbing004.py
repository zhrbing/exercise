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
# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('运行子进程%s(%s)...' % (name,os.getpid()))   #子进程执行代码
#
# if __name__=='__main__':
#     print('父进程%s' % os.getpid())
#     p=Process(target=run_proc,args=('test',))   #创建子进程:传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
#     print('子进程将启动')
#     p.start()
#     p.join()   #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#     print('子进程结束')
# #########################################################################################################
# from multiprocessing import Pool
# import os,time,random
#
# def long_time_task(name):
#     print('Run task %s (%s)' % (name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*5)
#     end=time.time()
#     print('Task %s runs %0.2f seconds.' % (name,(end-start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
# #########################################################################################################
# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
# #########################################################################################################












