class a:
    def display1(self):
        print("aiman")
    
class b(a):
    def display2(self):
        print("ali")
class c(b):
    def display3(self):
        super().display1()
        super().display2()
        print("shezan")
name=c()
name.display3()
