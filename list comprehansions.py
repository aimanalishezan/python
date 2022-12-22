#[expration for x in variable name that you want to comprehension]
num=[1,2,3,4,5]
result=[x*x for x in num]
print(result)
result1=[x for x in num if x%2==0]#filtering with comprension
print(result1)
