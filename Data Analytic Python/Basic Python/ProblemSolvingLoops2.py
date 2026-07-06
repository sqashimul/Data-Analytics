##1. Write a program to get Fibonacci series up to 10 numbers.
## 0+1+1+2+3+5+8+13
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(2, 11):
#     c = a + b
#     a = b
#     b = c
#     print(c)
#
# a = 0
# b = 1
# n  = int(input("Enter a number here: "))
# if n == 1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)
##2. Write a program to check if a number is prime or not.
## 1, 3, 11, 37. Number should be getter than 1, num>1, if num % i == 0, it's not prime, else: prime
# num = int(input("Enter a number here: "))
# if num <= 1:
#     print("It is not a prime number ")
# else:
#     for i in range (2, num):
#         if num % i == 0:
#             print("Number is not a prime number ")
#             break
#         else:
#             print("It is a prime number ")
#             break
##3. Write a program to find a palindrome of integers.
### Palindrome 131 = 131 (It's mean same number in opposite site )
### 333 == 333
# num = int(input("Enter a number here: "))
# temp = num
# rev = 0
# while num > 0:   ## num = number
#     dig = num % 10  ## dig = digit
#     rev = rev*10 + dig ## rev = reverse
#     num = num // 10
# if rev == temp:
#     print("It is a palindrome: ")
# else:
#     print("It is not a palindrome: ")
##4. Write a program to create an area calculator.
### Area Calculator
print("********AREA CALCULATOR******")
while True:
    print(""" Press 1 to get the area of square
    Press 2 to get the area of rectangle
    Press 3 to get the area of circle
    Press 4 to get the area of triangle """)

    choice = int(input("Enter a number between 1-4: "))

    if choice == 1:
        while True:
            side = float(input("Enter the length of one side: "))
            area = side**2
            print("The area of square is :", area)
            repeat = input("Do you want to try again with square? ")
            if repeat == "no":
                break

    elif choice == 2:
        while True:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length*width
            print("The area of rectangle is : ", area)
            repeat = input("Do you want to try again with rectangle? ")
            if repeat == "no":
                break


    elif choice == 3:
        while True:
            radius = float(input("Enter the radius of the circle: "))
            area = ((22/7)*(radius**2))
            print("The area of the circle is: ", area)
            repeat = input("Do you want to try again with circle? ")
            if repeat == "no":
                break


    elif choice == 4:
        while True:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter thee height of the triangle: "))
            area = 0.5*base*height
            print("The area of the triangle is: ", area)
            repeat = input("Do you want to try again with triangle? ")
            if repeat == "no":
                break
    repeat1 = input("Do you want to repeat the menu again? ")
    if repeat1 == "no":
        break

# import math
#
# print("********AREA CALCULATOR******")
# while True:
#     print("""
#     Press 1 to get the area of square
#     Press 2 to get the area of rectangle
#     Press 3 to get the area of circle
#     Press 4 to get the area of triangle """)
#
#     choice = int(input("Enter a number between 1-4: "))
#
#     # Validate the main choice first
#
#     if choice == 1:
#         while True:
#             side = float(input("Enter the length of one side: "))
#             area = side**2
#             print("The area of square is :", area)
#             repeat = input("Do you want to try again with square? (yes/no): ").lower()
#             if repeat == "no":
#                 break
#
#     elif choice == 2:
#         while True:
#             length = float(input("Enter the length of the rectangle: "))
#             width = float(input("Enter the width of the rectangle: "))
#             area = length * width
#             print("The area of rectangle is : ", area)
#             repeat = input("Do you want to try again with rectangle? (yes/no): ").lower()
#             if repeat == "no":
#                 break
#
#     elif choice == 3:
#         while True:
#             radius = float(input("Enter the radius of the circle: "))
#             # Using math.pi is more accurate than 22/7
#             area = math.pi * (radius**2)
#             print("The area of the circle is: ", area)
#             repeat = input("Do you want to try again with circle? (yes/no): ").lower()
#             if repeat == "no":
#                 break
#
#     elif choice == 4:
#         while True:
#             base = float(input("Enter the base of the triangle: "))
#             height = float(input("Enter the height of the triangle: "))
#             area = 0.5 * base * height
#             print("The area of the triangle is: ", area)
#             repeat = input("Do you want to try again with triangle? (yes/no): ").lower()
#             if repeat == "no":
#                 break
#
#     repeat1 = input("Do you want to repeat the menu again? (yes/no): ").lower()
#     if repeat1 == "no":
#         print("Thank you for using the Area Calculator!")
#         break
