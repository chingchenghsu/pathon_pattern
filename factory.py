import sys,os,math,collections
from math import *
class mybase:
        def __init__(self,aa, bb):
                self.a = aa
                self.b = aa
        def operation(self,aa,bb):
                print "base class",
        def make_operation(self,choice):
                print "I am here",
                if (choice == 1):
                        return Add
                else:
                        return Mult

class Add(mybase):
        def __init__(self):
                print "add"
        def operation(self,a,b):
                c = a+b
                return c,

class Mult(mybase):
        def __init__(self):
                print "mult"
        def operation(self,a,b):
                c = a*b
                return c,

class MakeOperation():
        def getOperation(self,choice,a,b):
                if choice=="+":
                        add = Add()
                        return add
                if choice=="*":
                        mult = Mult()
                        return mult
if __name__ == "__main__":
        mymake = MakeOperation()
        myobject = mymake.getOperation('*',4,2)
#       print myobject,
        answer = myobject.operation(4,2)
        print answer

