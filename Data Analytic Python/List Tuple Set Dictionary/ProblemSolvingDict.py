##Problem Solving Dictionary
"""#1. Write a Python program to sort a dictionary by value.
#2. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.
#3. Write a program to multiply all the items in a dictionary.
#4. Write a Python program to sort  a dictionary by key.
"""
# #1. Write a Python program to sort a dictionary by value.
# a = {"a":12, "b":23, "c":6, "d":91,"e":45}
# a = sorted(a.values())
# print(a)
#2. Write a Python script to print a dictionary where the keys are
# numbers between 1 and 15 and the values are square of keys.
# a = {}
# for i in range (1,16):
#     a[i] = i**2 ## a[i] = a of i; i*=i likha jete pare
#
# print(a)
#3. Write a program to multiply all the items in a dictionary.
# a = {"a":1, "b":2, "c":3, "d":4,"e":5}
# print(a["c"])
# product = 1 ## Multiplication er khetre 0 zero likha jabe na, tahole sob result 0 dekhabe
# for i in a:
#     product *= a[i] #Here value is multiplying
# print(product)

#4. Write a Python program to sort  a dictionary by key.
a = {12:"a", 56:"b", 23:"c", 48:"d", 91:"e"}

a = sorted(a.keys())
print(a)
