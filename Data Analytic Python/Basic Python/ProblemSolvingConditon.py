# Write a program to check if a number is positive
num = int(input("Enter a number here: "))
if num > 0:
    print("It is positive")

# Write a program to check whether a number is off or even.
num = int(input("Enter a number here: "))
if num % 2 ==0:
    print("It is an even number")
else:
    print("It is an odd number")
# Write a program to create area calculator
print("********AREA CALCULATOR******")
print(""" Press 1 to get the area of square
Press 2 to get the area of rectangle
Press 3 to get the area of circle
Press 4 to get the area of triangle""")

choice = int(input("Enter a number between 1-4:"))

if choice == 1:
    side = float(input("Enter the length of one side: "))
    area = side**2
    print("The area of square is :", area)

elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length*width
    print("The area of rectangle is : ", area)

elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = ((22/7)*(radius**2))
    print("The area of the circle is: ", area)

elif choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter thee height of the triangle: "))
    area = 0.5*base*height
    print("The area of the triangle is: ", area)

else:
    print("Invalid input")

# Write a program check whether the passed letter is a vowel or not.
letter = input("Enter a letter here: ")

##if letter in "aeiou":
##if letter in ("aeiou") or ("AEIOU"):
if (letter in "aeiou") or (letter in "AEIOU"):
    print("It is a vowel")
else:
    print("It is not a vowel")
# Write a program to check if a number is a single digit number, 2-digit number and so on.., up to 5 digits.
num = int(input("Enter a number here up to 5 digit: "))
if num >= 0 and num <= 9:
    print("It is a single digit number")
elif num >= 10 and num <= 99:
    print("It is a double digit number")
elif num >= 100 and num <= 999:
    print("It is a triple digit number")
elif num >= 1000 and num <= 9999:
    print("It is a four digit number")
else:
    print("It is a five digit number")


# একটি সংখ্যা জোড় নাকি বিজোড় তা পরীক্ষা করার ফাংশন
def জোড়_বিজোড়_পরীক্ষা(সংখ্যা):
    # সংখ্যাটিকে ২ দিয়ে ভাগ করলে যদি ভাগশেষ ০ হয়, তবে সেটি জোড়
    if সংখ্যা % 2 == 0:
        return "জোড় (Even)"
    # অন্যথায় সংখ্যাটি বিজোড়
    else:
        return "বিজোড় (Odd)"

# ব্যবহারকারীর কাছ থেকে ইনপুট নেওয়া
try:
    ইনপুট_সংখ্যা = int(input("একটি পূর্ণসংখ্যা লিখুন: "))
    ফলাফল = জোড়_বিজোড়_পরীক্ষা(ইনপুট_সংখ্যা)
    print(f"আপনার দেওয়া সংখ্যা {ইনপুট_সংখ্যা} হলো একটি {ফলাফল} সংখ্যা।")
except ValueError:
    print("দয়া করে একটি সঠিক পূর্ণসংখ্যা লিখুন।")
