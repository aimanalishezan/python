from random import randint
for x in range(1,6):
    guessnumber=int(input("Enter your guess between 1 to 5:"))
    randomnumber=randint(1,5)
    if guessnumber==randomnumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was:",randomnumber)