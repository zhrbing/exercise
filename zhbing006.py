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
# 使用MySQL
# import pymysql
# conn=pymysql.Connect(user='zhbing',
#                      passwd='123pwd',
#                      db='zhbingdb',
#                      charset='utf8')
# cursor=conn.cursor()
# # cursor.execute('create table person (id varchar(10) primary key,name varchar(20),phone_num varchar(11))')
# # cursor.execute('insert into person (id,name,phone_num) values (%s,%s,%s)',['001','陈媛媛','13000001111'])
# # cursor.execute('insert into person (id,name,phone_num) values (%s,%s,%s)',['002','陈媛媛','13011223344'])
# # cursor.execute("UPDATE person SET phone_num='13012345678',name='张冰' WHERE id='001'")
# # cursor.execute('select * from person where id=%s',('001'))
# cursor.execute('select * from person')
# values=cursor.fetchall()
# print(cursor.rowcount)
# print(values)
#
# conn.commit()
# cursor.close()
####################################################################################################
# import pymysql
# from sqlalchemy import Column,String,create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# Base=declarative_base()
#
# class User(Base):
#     __tablename__='person'
#
#     id=Column(String(10),primary_key=True)
#     name=Column(String(20))
#     phone_num=Column(String(11))
#
# engine=create_engine('mysql+pymysql://zhbing:123pwd@localhost:3306/zhbingdb?charset=utf8')
# DBsession=sessionmaker(bind=engine)
#
# session=DBsession()
# user=session.query(User).filter(User.id=='001').one()
# print(user)
# print('name:',user.name)
# print('phone:',user.phone_num)































