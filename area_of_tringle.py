import math
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if ((a+b)>c and (b+c)>a and (a+c)>b):
    s=a+b+c/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("area of a tringle is :",int(area))
else:
    print("tringular not possible")


