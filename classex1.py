try:
    class person():
        def __init__(self,name,age,gender="male"):#you can also define value here like this 
            self.name=name
            self.age=age
            self.gender=gender
        def info(self):
            print("name:",self.name,"age:",self.age,"gender:",self.gender)
    class fruit():
        def __init__(self,name,colour):
            self.name=name
            self.colour=colour
        def f(self):
            print("fruit name:",self.name,"colour:",self.colour)
    class nothing():
        pass #use the pass statement  to use it in future construct a body that does nothing.
    fruit1=fruit("apple","red")
    #del fruit1.colour      ***use this method for deleting the object properties
    fruit1.f()
    person1=person('aiman',19)
    person1.age=(20)#use this for modify the properties
    person1.info()
except TypeError:
    print("type error")
