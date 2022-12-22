while(1):
    from random import randint

    guessnumber=int(input("Enter your guess between 1 to 5:"))
    randomnumber=randint(1,6)
    if guessnumber==randomnumber:
        print("you have won")
    else:
        print("you gave lose")
        print("the guess number is:",int(randomnumber))
