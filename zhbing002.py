# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

#面向对象编程
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))

    def print_grade(self):
        if self.score>=90:
            print('A')
        elif self.score>=60:
            print('B')
        else:
            print('C')

bart=Student('Bart Simpson',59)
bart.print_score()
bart.print_grade()













