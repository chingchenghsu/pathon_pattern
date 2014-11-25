import sys,os,math,collections
from math import *

class Mybase:
        def __init__(self):
                pass
        def operation(self):
                print"base class, do nothing"
class Add(Mybase):
        def operation(self,aa,bb):
                cc =aa+bb
                return cc
class Sub(Mybase):
        def operation(self,aa,bb):
                cc =aa-bb
                return cc
class Mult(Mybase):
        def operation(self,aa,bb):
                cc =aa*bb
                return cc
class Content:
        def __init__(self,Mybase):
                self.mybase = Mybase
        def Contentoperation(self,a,b):
                return self.mybase.operation(a,b)

if __name__=="__main__":
        myadd = Add()
        mysub = Sub()
        mymult = Mult()
        mycontent = Content(myadd)
        print mycontent.Contentoperation(3,4)
        mycontent = Content(mysub)
        print mycontent.Contentoperation(3,4)
        mycontent = Content(mymult)
        print mycontent.Contentoperation(3,4)
