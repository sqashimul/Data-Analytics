## For Loop with Conditional Statements
## The use of if-else statements increases the ability of for loop to completes the task effectively.
## By using if-else statements we can provide with special conditions inside for loop.
# for i in range (1, 11):
#     if i == 3:
#         print("Add this song to the favourite ")
#     else:
#         print(i)

for i in range (1, 101): #Common multiple any 2 numbers
    if i % 8 == 0 and i % 12 == 0:
        print(i)
