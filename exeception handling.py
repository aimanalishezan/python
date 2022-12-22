try:
    list=[20,0,30]
    result=list[0]/list[2]
    print(result)
    print("Done")
except ZeroDivisionError:#When a programm is error use this for result
    print("divison zero is not possible")
except IndexError:
    print("indx error")
finally:#use this keyword when you must want that perticular code to run 
    print("unsuccecsfull")
"""
when a error came type execpt and the "error name":

"""

