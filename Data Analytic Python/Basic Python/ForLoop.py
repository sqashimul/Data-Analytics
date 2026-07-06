## For loop is a loop that repeats something in a given range.
## The range has a starting point, ending point and a step/gap in it.
## +1 is added to the ending point while defining range.

# for i in range (1,6):
#     print(i)
# for i in range (1,6,2):
#     print(i)
# for i in range (1,19,3):
#     print(i)
# for i in range (2,9,2):
#     print(i)
# for i in range (1,6):
#     print("Hello World")
# for i in range (1,6,2):
#     print("Hello World")
#### '7 times Table' Multiplication of table 7
# n = 7
# for i in range (1,11):
#     print(n,"x",i,"=",n*i)
###Others Tables of Multiplication
n = int(input("Enter a number here: "))
for i in range (1,11,2): ###If I need odd number then (1,11,2)
    print(n,"x",i,"=",n*i)

    
