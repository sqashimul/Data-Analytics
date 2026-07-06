## Return Statement and Recursion in Python
"""
Return Statement:
    Return keyword in python is used to exit a function and return the value of the function

"""
# def hello():
#     return ("Hello world")
#     #Return Statement
# print(hello())
#
# def add(a,b):
#     # return (a+b)
#     return ("The addition of two numbers is:",a+b)
#     # return "The addition of two numbers is:",a+b
#
# print(add(12,5))

"""
Recursion in Python:
    Recursion in most commonly used mathematical and programming concept.
    In simple words, recursion means a function can call itself, giving us a benefit of looping through data in order to get result.
"""
## Bar bar nijeke call korai hocche Recursion function
# def hello():
#     print("Hi Simul")
#     return hello()
# print(hello())

# Factorial 5! = 5*4*3*2*1 = 120; 5! = 5 * 4! Same things
# n * (n-1)!
def fact (n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

print(fact(5))
print(fact(4))
print(fact(3))

# Advantage and Disadvantage of Recursion
"""
Advantages:
    1. They make the code look clean and organized.
    2. By the use of recursive functions, a complex task can be broken down into small sub - parts.
    3. Sequence generation becomes easier.
Disadvantages:
    1. Recursive Python Functions take up a lot of memory.
    2. Sometimes the logic becomes hard to follow.
    3. Recursive function debugging sometime it's difficult. 
"""