class tringle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calculate_area(self):
        area=0.5*self.base*self.height
        print("Area =",area)
t1=tringle(10,20)
t1.calculate_area()
t2=tringle(20,30)
t2.calculate_area()
