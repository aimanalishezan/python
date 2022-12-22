#xxargument works like dictionary
def student(**details):#use two stricts(**) number for xxargument
    print(details["id"])
student(id=101,name="anis")
