class car():
    def __init__(self,engine):
        self.engine=engine
class type(car):
    def __init__(self,power,engine):
        super().__init__(engine)
        self.power=power
class onway(type):
    def __init__(self,engine,power,name):
        super().__init__(engine,power)
        self.name=name
    def show(self):
        print("engine",self.engine,"power",self.power,"name",self.name)
mycar=onway("1000cc","500hp","mercedies")
mycar.show()

