#when a function do different works on diffrent situation then that called polymorphisom
#bult in polymorphic function
print(len("aiman ali shezan"))#here len is a polymorphisom
print(len([10,20,30]))
#user defined polymorphisom
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):#here display is a polymorphisom beacuse its use for different works on method
        pass
class ob(person):
    def display(self):
        print("name=",self.name)
        print("age=",self.age)
class ob2(person):
    def display(self):
        age=self.age + 2
        print("Age is ",age)
m=ob("aiman",20)
m.display()
m1=ob2("mim",10)
m1.display()
