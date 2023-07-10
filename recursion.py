#recursion  is a function where function can call itself
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
i=int(input("enter any number:"))
print(fact(i))
