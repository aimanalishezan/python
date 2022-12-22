#xargument works like tupple
def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print(sum)
add(10,20,30,30)
