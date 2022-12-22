class a:
    def display(self):
        print("aiman")
class b:
    def display(self):
        print("ali")        
class c(b,a):#if the class function name  was same then the first super class will works that you provides
    """
    def display():
        print("shezan")
    """
    pass
name=c()
name.display()
