#you can use this program to input data in list
n=int(input("Enter list last number:"))
i=0
numbers=[]
while i<=n:
    
    b=i
    print(b)
    i=i+1
    numbers.extend([b])

for i in numbers:
    square=i**2
    print("square of:",i,"is",square)

