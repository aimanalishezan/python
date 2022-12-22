#use of and oparator 
num1=int(input("Enter num 1:"))
num2=int(input("Enter num 2:"))
num3=int(input("Enter num 3:"))
if num1>num2 and num1>num3:
    print("large number is:",num1)
elif num2>num1 and num2>num3:
    print("large number is:",num2)
else:
    print("large number is:",num3)

#use of or oparator 
ch = 'm'
if ch == 'a'or ch=='e'or ch=='i'or ch=='o'or ch=='u':
    print("vowel")
else:
    print("consonent")