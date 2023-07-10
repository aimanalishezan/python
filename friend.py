"""import math
def fact(n=5):
    r=math.factorial(n)
    print(r)
fact()
"""
'''def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
n=10
print("fibo series")
for i in range(n):
    print(fibo(i),end=" ")
'''
"""def fibo():
    n=1
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fibo()
"""
import math
a=float(input("enter number a:"))
b=float(input("enter number b:"))
c=float(input("enter number c:"))
d=b*b-4*a*c
if d==0:
    print("x="-b/2*a)
elif d>0:
    x1=print(-b+math.sqrt(d)/2*a)
    x2=print(+b+math.sqrt(d)/2*a)
    print(x1,x2)
else:
    print("roots are imaginary")
