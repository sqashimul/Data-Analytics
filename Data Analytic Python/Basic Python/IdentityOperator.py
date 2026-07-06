# Identity Operator
a = 1234
b = "1234"
c = 1234
print(a is b)
print(a is not c)
print(a is c)

x = [10, 20]
y = [10, 20]

if x is not y:
    print("x and y are separate objects")  # This will print

# Small integers share memory locations
num1 = 100
num2 = 100
print(num1 is num2)  # True

# Larger integers do not share memory locations
num3 = 500
num4 = 500
print(num3 is not num4)  # False (Use num3 =! num4 instead!)
