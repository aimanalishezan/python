import math
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=(b*b)-(4*a*c)
if d==0:
    x=-b/(2*a)
    print(x)
elif d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print(float(x1),float(x2))
else:
    print("not possible (-_-)")

