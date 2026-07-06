# Assignment Operators
# Assignment Operators are used in Python to assign values to variables
# a = 6 is a simple assignment operator that assigns the value 6 on the right to the variable 'a' on the left.
# Operator : Example : Equivalent to
#   =      x=6        x=6
#   +=     x+=6       x = x+6
#   -=     x-=6       x = x-6
#   *=     x*=6       x = x*6

# Directly assigns 10 to x
x = 10
print(x)  # Output: 10

#1. Simple Assignment
# Directly assigns 10 to x
x = 10
print(x)  # Output: 10
#2. Addition Assignment
x = 10
x += 5  # Same as: x = x + 5
print(x)  # Output: 15

#3. Subtraction Assignment
x = 10
x -= 3  # Same as: x = x - 3
print(x)  # Output: 7
#4. Multiplication Assignment
x = 10
x *= 2  # Same as: x = x * 2
print(x)  # Output: 20
#5. Division Assignment
x = 10
x /= 4  # Same as: x = x / 4 (always returns a decimal float)
print(x)  # Output: 2.5
#6. Floor Division Assignment
x = 10
x //= 4  # Same as: x = x // 4 (divides and chops off decimals)
print(x)  # Output: 2
#7. Modulus Assignment
x = 10
x %= 3  # Same as: x = x % 3 (returns the remainder of 10 / 3)
print(x)  # Output: 1
#8. Exponentiation Assignment
x = 10
x **= 3  # Same as: x = x ** 3 (10 raised to the power of 3)
print(x)  # Output: 1000
#9. Bitwise AND Assignment
x = 5   # Binary: 0101
x &= 3  # Binary: 0011 (Evaluates 0101 & 0011)
print(x)  # Output: 1 (Binary: 0001)
#10. Bitwise OR Assignment
x = 5   # Binary: 0101
x |= 3  # Binary: 0011 (Evaluates 0101 | 0011)
print(x)  # Output: 7 (Binary: 0111)
#Bitwise XOR Assignment
x = 5   # Binary: 0101
x ^= 3  # Binary: 0011 (Evaluates 0101 ^ 0011)
print(x)  # Output: 6 (Binary: 0110)
#12. Bitwise Right Shift Assignment
x = 5    # Binary: 0101
x >>= 1  # Shifts bits 1 place right (becomes 0010)
print(x)  # Output: 2S
#13. Bitwise Left Shift Assignment
x = 5    # Binary: 0101
x <<= 1  # Shifts bits 1 place left (becomes 1010)
print(x)  # Output: 10
#14. Walrus Operator (Assignment Expression)python# Assigns value to 'length' AND checks condition at the exact same time
if (length := len("Python")) > 5:
    print(f"Long word with {length} letters.")  # Output: Long word with 6 letters.


