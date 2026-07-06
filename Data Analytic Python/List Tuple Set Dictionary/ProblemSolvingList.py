A = ["Ross", "Rachel", "Monica", "Joe"]
# 1. Write a program to swap first and forth element.
# 2. Write a program to add a new value at second position.
# 3. Write a program to delete a value form 3rd position.
B = [13, 7, 12, 10]
# 1. Write a program to multiply all the numbers in the list.
# 2. Write a program to get the largest number from the list.
# 3. Write a program to get the smallest from the list.

A = ["Ross", "Rachel", "Monica", "Joe"]
# # 1. Write a program to swap first and forth element.
A[0],A[3] = A[3],A[0]
print(A)

# # 2. Write a program to add a new value at second position.
A.insert(1, "Phoebe")
print(A)
# # 3. Write a program to delete a value form 3rd position.
A.pop(2)
print(A)
B = [13, 7, 12, 10]
# # 1. Write a program to multiply all the numbers in the list.
# mul = 1
# for i in (B):
#     mul*=i
#     print(mul)
# print(mul)
# # 2. Write a program to get the largest number from the list.

B.sort() # Arrange the Ascending order
print(B)
print("The largest value in the given list", B[-1])
print("The smallest value in the given list is", B[0])
 # # 3. Write a program to get the smallest from the list.
B.sort() # Arrange the Ascending order
print(B)
print("The smallest value in the given list", B[-1])
