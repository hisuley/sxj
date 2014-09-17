__author__ = 'pc'

#decprator

class MyClass:

    @staticmethod
    def smeth():
        print "This is a static method"

    @classmethod
    def cmeth(cls):
        print "This is a class of ", cls

MyClass.smeth()
MyClass.cmeth()

#__setattr__ and __getattr__

class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name = size:
            self.width, self.height = value
        else:
            self__dict__[name] = value

    def __getattr__(self, item):
        if name = 'size':
            return self.width, self.height
        else:
            raise AttributeError

#iterator

class Fibs:

    def __init__(self):
        self.a = 0
        self.b = 0

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    @property
    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break

#yield

def fab(maxnumber):
    n, a, b = 0, 0, 1
    while n < maxnumber:
        yield b
        a, b = b, a+b
        n += 1

#yield

def flatten(nested):
    try:
        try:
           nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in sublist:
                yield element
    except TypeError:
        yield nested


nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print num
