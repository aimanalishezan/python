class student:
    roll=""
    gpa=""
    def setvalue(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll:{self.roll}, gpa:{self.gpa}")
aiman=student()
aiman.setvalue(602832,3.87)
aiman.display()
