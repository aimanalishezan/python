#use this mathod if want to run the programe with errors
while(1):
    try:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        result=a/b
        print(int(result))
    except(ValueError,ZeroDivisionError):
        print("you have entered incorrect input...")
    finally:
        print("enter an valid input")
