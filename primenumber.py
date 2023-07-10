n=int(input("enter the number:"))
print("prime number is")
for i in range(2,n+1):
    for j in range(2,i-1):
        if(i%j==0):
            break
    else:
        print(i)

