### Creation of Modules
"""
To create a module, all you need to do is create a .py file in a simular path to your python file.
Insider that file, you can add required functions you need your program to perform.

To call the module inside your program, all you need to do is use import keyword followed by the name of your.py file.
"""
import module_01

a = module_01.add(2,3)
print(a)

# Create Alias
import module_01 as mold

b = mold.add(5,22)
print(b)

c = mold.employee["Name"]
print(c)
