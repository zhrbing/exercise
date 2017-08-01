# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

# 使用SQLite
# import sqlite3
# conn=sqlite3.connect('test.db')
# cursor=conn.cursor()
# cursor.execute('create table user (id varchar2(20) primary key,name varchar2(20))')
# cursor.execute('insert into user (id,name) values(\'1\',\'Michael\')')
# cursor.execute('insert into user (id,name) values(\'2\',\'Cindy\')')
# print(cursor.rowcount)

# cursor.execute('select * from user where id=?',('2',))
# values=cursor.fetchall()
# print(values)

# cursor.execute('select * from user')
# values2=cursor.fetchall()
# print(values2)
# for i in values2:
#     print(i)
# 
# cursor.close()
# conn.commit()
# conn.close()
####################################################################################################
