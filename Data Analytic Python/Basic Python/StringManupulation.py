## STRING
""" String are the combination of number, symbols and letters, enclosed inside quotations.

Creation of a String: Strings can be created by enclosing numbers, letters, or special symbols
inside double quotations.
It means assigning a string value to a variables.
a = ("hello world")
print (a)
"""
from operator import index

""" length, count, upper, lower, index, capitalize, casefold
find, format, center"""

a = "Harry Potter and the Goblet of Fire"
print(type(a))
print(a)
## to find the length of the string
print(len(a))
## to find the number of times a character is occurring
print(a.count("o"))
print(a.count("H"))
## to convert each letter into upper case
print(a.upper())
## to convert each letter into Lower case
print(a.lower())
## to find the index of any character
print(a.index("o", 15,34))
b = "harry potter and the goblet of fire"
## to conver the first letter to capital
print(b.capitalize())
c = "Harry Potter And The Goblet Of Fire"
## to convert c string into lower case
print(c.casefold())
## to find the index number of a character
print(c.find("o", 15, 34))
## to write variables inside a string
name = "Jhon"
age = 24
b = "My name is {}. and my age is {}"
print(b.format(name, age))
## it fills the given characters and centralizes a string
print(name.center(20))
print(name.center(20, "*"))