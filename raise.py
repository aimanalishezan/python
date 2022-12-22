def voter(age):
    if age<18:
        raise ValueError("invalid voter")
    return "you are allowed to vote"
n=int(input("Enter year:"))
try:
    print(voter(n))
except ValueError as n:
    print(n)

