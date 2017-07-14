# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

#內建模块--datetime
from datetime import datetime,timedelta,timezone    #导入datetime模块的类
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







