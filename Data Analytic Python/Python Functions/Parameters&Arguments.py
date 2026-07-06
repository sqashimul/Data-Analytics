## Parameters & Arguments
"""
Parameters:
    Parameters are the variables written inside the parentheses with the name of function.
Arguments:
    Arguments are the values passed to the parameters while calling the function.
"""
def add(x,y): ## Parameters
    ## Function er namer sathe jokhon variables likha hoy tokhon take Parameters bole.
    ## Here x & y parameters
    print(x+y)

    ## ar jokhon functin er moddhe jokhon value provide kora hoy tokhon take arguments bole
add(2,3) ## Here 2 & 3 is Arguments
add(4,7)

def rect(length, width):
    print("the area of the rectangle is", length*width)

rect(12,3)

#Arbitray Arguments
def hello(name):
    print("Hello, my name is", name)

hello("john")
#Arbitary Arguments
def hi(*name):
    print("Hi, my name is", name[2])

hi("John", "Lisa", "Petter")