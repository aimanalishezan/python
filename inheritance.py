#inheritance use to re use the code of class if it already exits in code
#here phone is paren class,super class,base class
#nokia is sub class,child class
#the class you inherite call paren or base class
class phone:
    def call(self):
        print("you can call now")
    def massage(self):
        print("you can massage now")
class nokia(phone):#here nokia is sub class of phone
    """
    def call(self):
        print("you can call now")
    def massage(self):
        print("you can massage now")
    """
    def photo(self):
        print("you can take photo")
n=nokia()
n.call()
n.massage()
n.photo()
print(issubclass(nokia,phone))

