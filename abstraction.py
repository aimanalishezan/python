#when you create a method  not used as a object and use it in different class that called abstraction
from abc import ABC,abstractclassmethod
#when you create a abstract class you cant create object for that calss
#if any class inherite tha paren class you need to call the abstrack method
class shape(ABC):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        abstractclassmethod
        def area(self):
            pass
class tringle(shape):
    def area(self):
        area=0.5*self.base*self.height
        print("area is ",area)

t=tringle(6,8)
t.area()
