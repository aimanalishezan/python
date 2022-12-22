class shape():
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area():
        print("I am area method of shape")
class tringle(shape):
    def area(self):
        area=0.5*self.base*self.height
        print("area of tringle is :",area)
class rectangle(shape):
    def area(self):
        area=self.base*self.height
        print("area of rectangle is :",area)
tringle1=tringle(20,30)
tringle1.area()
rectangle1=rectangle(20,30)
rectangle1.area()


    
