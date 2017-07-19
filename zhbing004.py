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

# from multiprocessing import Process,Queue
# import os,time,random
#
# def write(q):
#     print('Process to write:%s' % os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print('Process to read:%s' % os.getpid())
#     while True:
#         value=q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()
# #########################################################################################################
#线程
# import time,threading
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n=0
#     while n<5:
#         n+=1
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t=threading.Thread(target=loop,name='LoopThread') #启动一个线程:传入一个函数并创建Thread实例，然后调用start()开始执行
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
# #########################################################################################################
#正则表达式
import re
# def user_match(user_print):
#     if re.match(r'^\d{3}\-\d{3,8}$',user_print):
#         print('Match success!')
#     else:
#         print('Not match!')
#
# user_print=input('请输入电话号码，格式：xxx-xxxxxx：')
# user_match(user_print)

# print(re.split(r'[\s\,]+','a b ,  c,d  e 1,2   3    4'))  #切分字符串

# m=re.match(r'^(\d{3})-(\d{3,8})$',input('请输入电话号码，格式：xxx-xxxxxx：'))
# print(m)
# print(m.group(0))  #原始字符串
# print(m.group(1))  #提取子串
# print(m.group(2))

# t=input('请输入时间，格式：xx:xx:xx：')
# m= re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# print(m.groups())

# print(re.match(r'^(\d+)(0*)$','102300').groups())  #贪婪匹配,\d+直接把后面的0全部匹配了，结果0*只能匹配空字符串了
# print(re.match(r'^(\d+?)(0*)$','102300').groups())  #加?:非贪婪匹配

# re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')  #编译
# print(re_telephone.match('010-12345').groups())
# print(re_telephone.match('010-8086').groups())
# #########################################################################################################
sum=0
with open('file.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        # print(line.strip())
        m=re.sub('\D','',line.strip())   #提取字符串中的数字
        # print(re.findall(r"\d+\.?\d*", string))
        print(m)
        sum+=int(m)

print(sum)

