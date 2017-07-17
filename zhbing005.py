# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

#內建模块--datetime
# from datetime import datetime,timedelta,timezone    #导入datetime模块的类
# now=datetime.now()        #获取当前datetime
# print(now,'\t',type(now))

# dt=datetime(2017,7,14,14,32)  #用指定日期时间创建datetime
# print(dt)
# print(datetime.now().timestamp())  #把datetime转换为timestamp，小数位表示毫秒数

# t=1429417200.0
# print(datetime.fromtimestamp(t))    #timestamp转换为datetime,本地时间
# print(datetime.utcfromtimestamp(t)) #UTC标准时区时间

#str转换为datetime
# str='2015-6-1 18:19:59'
# cday=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
# print(cday,type(cday))

#datetime转换为str
# now=datetime.now()
# str1='%a,%b %d %H:%M'
# str2='%Y-%m-%d %H:%M:%S'
# print(now.strftime(str1))
# print(now.strftime(str2))

#datetime加减
# now=datetime.now()
# print(now)
# print(now+timedelta(hours=3))
# print(now-timedelta(days=2))
# print(now+timedelta(days=2,hours=3))

# tz_utc8=timezone(timedelta(hours=8))    #创建时区UTC+8:00
# now=datetime.now()
# print(now)
# dt=now.replace(tzinfo=tz_utc8)  #强制设置为UTC+8:00
# print(dt)
#如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区

# utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
# print('UTC时间：',utc_dt)   # 拿到UTC时间，并强制设置时区为UTC+0:00
#
# bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
# print('北京时间：',bj_dt)    # astimezone()将转换时区为北京时间
#
# tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
# print('东京时间：',tokyo_dt) # astimezone()将转换时区为东京时间
#
# tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
# print('东京时间：',tokyo_dt2)    # astimezone()将转换时区为东京时间

################################################################################
#內建模块collections
#namedtuple
# from collections import namedtuple
# Point=namedtuple('Point',['x','y']) # namedtuple('名称', [属性list])
# p=Point(1,2)
# print(p.x,p.y)
# print(isinstance(p,Point),isinstance(p,tuple))

#deque:高效实现插入和删除操作的双向列表，适合用于队列和栈
# from collections import deque
# q=deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)
# q.popleft()
# print(q)
# q.pop()
# print(q)

#计数器Counter
# from collections import Counter
# cnt=Counter()
# for ch in 'programming developing':
#     cnt[ch]+=1
#
# print(cnt)
################################################################################
#hashlib
import hashlib

#md5生成结果是128bit，通常用32位16进制字符串表示
md5=hashlib.md5()

# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# md5.update('123456'.encode('utf-8'))
# print(md5.hexdigest())

#分块多次调用，计算结果一样
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

#sha1生成结果是160bit，通常用40位16进制字符串表示
# sha1=hashlib.sha1()
# sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())
################################################################################
#itertools
import itertools
# ns=itertools.repeat('ABC',8)  #第二个参数限定重复次数
# for n in ns:
#     print(n)

# natuals=itertools.count(1)
# ns=itertools.takewhile(lambda x:x<=10,natuals)
# for n in ns:
#     print(n)

#串联迭代对象
# for c in itertools.chain('ABC','XYZ'):
#     print(c)

#把迭代器中相邻的重复元素挑出来放在一起
# for key,group in itertools.groupby('AAABBBCCAAA'):
#     print(key,list(group))

#忽略大小写分组
# for key,group in itertools.groupby('AaaBBcCcAAa',lambda c:c.upper()):
#     print(key,list(group))
################################################################################
#contextlib
from contextlib import contextmanager

# class Query(object):
#
#     def __init__(self,name):
#         self.name=name
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q=Query(name)
#     yield q
#     print('End')
#
# with create_query('Bob') as q:
#     q.query()

#在代码前后自动执行特定代码
# @contextmanager
# def tag(name):
#     print('<%s>' % name)
#     yield
#     print('<%s>' % name)
#
# with tag('h1'):
#     print('hello')
#     print('world')

# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('https://www.baidu.com')) as page:
#     for line in page:
#         print(line)
################################################################################
#urllib

# from urllib import request

# url='https://api.douban.com/v2/book/2129650'
# with request.urlopen(url) as f:
#     data=f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print('Data:',data.decode('utf-8'))

# url='http://www.douban.com/'
# add_header='Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
# req=request.Request(url)
# req.add_header('User-Agent', add_header)
# with request.urlopen(req) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print('Data:',f.read().decode('utf-8'))
################################################################################





















