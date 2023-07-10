#1*1+3*2+5*3+.............n*n
n=int(input("enter last number :"))
sum=0
for i in range(1,n+1,2):
    sum=sum+i**i
    print(i,sum)
