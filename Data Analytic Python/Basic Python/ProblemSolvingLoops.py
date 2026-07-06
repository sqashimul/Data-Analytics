####********** Loops Problem Solving **********
### 1. Write a program to find a sum of all the even numbers up to 50.
sum = 0
for i in range (1,51):
    if i % 2 == 0:
        sum  += i

# print("The sum of all even number up to 50 is :", sum)
### 2. Write a program to write first 20 numbers and their squared numbers.
for i in range (1,21):
    print(i, i**2)

### 3. Write a program to find sum of first 10 odd numbers using while loop.
sum = 0
n = 0
while n <= 20:
    if n  %2 != 0:
        sum += n
    n += 1
print("The sum of first 10 odd numbers is :", sum)

### 4. Write a program to check if a number is divisible by 8 and 10 up to 100 numbers.
for i in range (1,100):
    if i % 8 == 0 and i % 12 == 0:
        print(i)
### 5. Write a program to create a billing system at supermarket.
while True:
    name = input("Enter Customer's name: ")
    total = 0

    while True:
        print("Enter the amount and quantity ")
        amount = float(input("Enter Amount: "))
        quantity = float(input("Enter Quantity: "))
        total += amount * quantity
        repeat = input(("Do you want to add more items? (yes/no): "))
        if repeat == "no" or repeat == "No":
            break

    print("-" *40)
    print("Name: ", name)
    print("Amount to be paid: ", total)
    print("-" *40)
    print("******Happy Shopping******")

    repeat1 = input("Do you want to go to next customer? (yes/no): ")
    if repeat1 == "no" or repeat1 == "No":
        break