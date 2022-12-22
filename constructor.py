#constructor is a  spacial type of method which dont need to call 
class student:
    roll=""
    gpa=""
    def __init__(self,roll,gpa):#use __ it two times for __init__ function
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll:{self.roll}, gpa:{self.gpa}")
aiman=student(32,3.89)
aiman.display()
mim=student(33 ,3.12)
mim.display()
