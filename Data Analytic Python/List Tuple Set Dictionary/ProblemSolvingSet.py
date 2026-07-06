## Problem Solving in Set
"""
1. Write a program to find max and min in a set.
2. Write a program to find a common elements in three lists using sets.
3. Write a program to find difference between two sets.
4. Write a Python program to remove an item from a set if it is present in the set.
5. Write a Python program to check if a set is a sub-set of another set.
"""
# 1. Write a program to find max and min in a set.
a = {12,56,34,8,90,1,57}
maximum = max(a)
minimum = min(a)
print("The minimum value in the set is: ",minimum)
print("The maximum value in the given set is: ", maximum)
# 2. Write a program to find a common elements in three lists using sets.
a = [1,5,6,8,2]
b = [4,5,6,7]
c = [1,9,6,2,5]

print("The common elements in the give three lists are:",set(a) & set(b) & set(c))
# 3. Write a program to find difference between two sets.
a = {1,5,6,8,2}
b = {1,9,6,2,5}

print(a.difference(b))
print(b.difference(a))
# 4. Write a Python program to remove an item from a set if it is present in the set.
a = {1,5,6,8,2}
a.discard(8)
print(a)
# 5. Write a Python program to check if a set is a sub-set of another set.
a = {1,2,3,4,5,6,}
b = {2, 3, 4}
print(b.issubset(a))
print(a.issubset(b))