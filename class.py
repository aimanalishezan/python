class student:#create a object or template so that you can call it any time
    roll=""
    gpa=""
aiman=student()#call object
aiman.roll=602832
aiman.gpa=3.89
print(f"aiman\nroll:{aiman.roll}\ngpa:{aiman.gpa}")
mim=student()#call object
mim.roll=0000
mim.gpa=4
print(f"mim\nroll:{mim.roll}\ngpa:{mim.gpa}")
