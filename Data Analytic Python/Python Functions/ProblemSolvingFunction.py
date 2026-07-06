## Problem Solving in Functions
"""
1. Write a function to find maximum of three numbers in Python.
2. Write a Python function to create and print a list where the values are
   square of numbers between 1 and 30.
3. Write a Python function that takes a number as a parameter and check if the number is prime or not.
4. Write a Python function to sum all the numbers in a list.
5. Write a Python program to solve the Fibonacci Sequence using Recursion.
"""
## 1. Write a function to find maximum of three numbers in Python.
# def maximum_num (val1, val2, val3):
#     if val1 > val2 and val1 > val3:
#         print(val1, "Is the gratest number")
#     elif val2 > val1 and val2 > val3:
#         print(val2, "is the greatest number")
#     else:
#         print(val3, "is the greatest number")
#
# maximum_num(12, 5, 9)
# maximum_num(4,5,8)
# 2. Write a Python function to create and print a list where the values are
#square of numbers between 1 and 30.
# def create_list():
#     l = []
#     for i in range(1, 31):
#         l.append(i**2)
#
#     return l
# print(create_list())
## 3. Write a Python function that takes a number as a parameter and check if the number is prime or not.
# def check_prime(num):
#     if num == 1:
#         print("It is not a prime number")
#     if num == 2:
#         print("It is a prime number ")
#     if num > 2:
#         for i in range (2, num):
#             if num % i == 0:
#                 print("It is not a prime number")
#                 break
#         else:
#             print("It is a prime number")
# check_prime(37)
# check_prime(10)
# check_prime(11)
## 4. Write a Python function to sum all the numbers in a list.
# def add(numbers):
#     total = 0
#     for i in numbers:
#         total = total+i
#     return (total)
# print(add([12,4,5,6,7,8]))
# print("The sum of all the items in the list is ",add([154,4,50,6,9,7]))
# ## Solution 2 (Using Recursion)
# def add2(numbers):
#     if len(numbers) == 1:
#         return (numbers[0])
#     else:
#         return (numbers[0] + add2(numbers[1:]))
#
# print(add2([12,4,5,6,7,8]))
##5. Write a Python program to solve the Fibonacci Sequence using Recursion.
def fibuseri(num):
    if num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        return (fibuseri(num-1) + fibuseri(num-2))
print(fibuseri(7))
print(fibuseri(9))
print(fibuseri(8))