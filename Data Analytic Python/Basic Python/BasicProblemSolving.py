# Write a program to display a person's name, age and address in three different lines.
name = "Jhon"
age = 25
address = "H: 45, Road: 05, Block:B"
print(name, age, address)
print(name)
print(age)
print(address)
#Write a program to swap two variables.
## Method 1
x = 12
y = 13

temp = x
x = y
print(temp)
x = y
print(x)
y = (temp)
print(y)
print("Value of x is", x)
print("Value of y is", y)


##Method 2

a = 30
b = 15

## left, right = right, left
a,b = b,a
print(b)
print(a)

#  Write a program to convert a float into integer.
x = 12.4
print(type(x))

x = int(x)
print(type(x))
print(x)

# Write a program to take details from a student for ID-Card and then print it in different lines.
Name = input("Enter the name of the Student: ")
Grade = input("Enter the grade of the Studetn: ")
age = int(input("Enter the age of the Student: "))
email = input("Enter the email of the studet: ")
Phone_No = input("Entert the phone number of the Student: ")
print("Student Identity Card")
print("Name: ",Name)
print("Grade: ",Grade)
print("Age: ", age)
print("E-mail: ", email)
print("Phone Number: ", Phone_No)

# Write a program to take an user input as integer then convert it to float.
a = int(input("Enter a number here: "))
print(a)
print(type(a))

a = float(a)
print("After Conversion: ", a)
print(type(a))

