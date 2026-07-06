## Local and Global Variables
"""
Local Variables:
Local Variables are restricted to only one block of code and cannot be changed throughout the program.

Global Variables:
Global variables are not restricted to one block of code and then can be changed throughout the program.
"""
#Local Variables:
x = 24
print("The first Variable x: ", x)
def exe():
    x = 25
    return x
print(exe())
print(x)
## Global Variables
y = 24
print("The first Variable x: ", y)
def yey():
    global y
    y = 25
    return y
print(yey())
print(y)