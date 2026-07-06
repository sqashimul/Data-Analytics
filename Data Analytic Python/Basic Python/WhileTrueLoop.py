### It is an infinite loop
### To break a while true loop, break statement is used.
# while True:
#     print("hello")
# n = 1
# while True:
#     print(n)
#     n +=1
#     # break
#
while True:
    num1 = int(input("Enter a number here: "))
    num2 = int(input("Enter a another number here: "))

    print(num1 + num2)
    repeat = input("Do you want to stop the program: ")
    if repeat == "yes":
        break


