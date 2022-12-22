def square(x):
    return x*x
num=[1,2,3,4,5]
result=list(map(square,num))#map function can receive function and list or etarable object
print(result)
