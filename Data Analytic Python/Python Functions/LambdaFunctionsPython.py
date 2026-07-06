# Lambda Function in Python
"""
--> It is used when an anonymous function is required for a short period of time.
--> It can take numerous arguments
--> It can only have one expression.
"""

a = lambda b: b*5 # Here lambda b is an anonymous function
print(a(4))

x = lambda a, b, c: (a+b)*c
print(x(3,7,3))
