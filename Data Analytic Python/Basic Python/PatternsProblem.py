### Write a program to display this pattern.
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# for i in range (1,6): #rows
#     for j in range (1,6): #columns
#         print(j, end = " ")
#     print()
# ## Write a program to display this pattern.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range (1,6): ##rows
#     for j in range (1,i+1): ##columns
#         print(j, end = " ") ##Number ke liyea j de raha hu, Number obtain j
#     print()
### Write a program to display this pattern.
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range (1,6): ##rows
#     for j in range (1,i+1): ##columns
#         print("*", end = " ") ## iha pe number ke jaygay * pattern de raha, jake * show kare ga
#     print()

# ## Write a program to display this pattern.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range (1,6): ##rows
#     for j in range (1,i + 1): ##columns
#         print(i, end = " ")
#     print()

# ## Write a program to display this pattern.
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# for i in range (1,6): ##rows
#     for j in range (6, i, -1): ##columns
#         print(i, end = " ")
#     print()
# for i in range (1,6): ##rows
#     for j in range (6, i, -1): ##columns
#         print(j, end = " ")
#     print()
# for i in range (1,6): ##rows
#     for j in range (6, i, -1): ##columns
#         print("*", end = " ")
#     print()
# ## Write a program to display this pattern.
#      *
#     **
#    ***
#   ****
#  *****
# for i in range (1,6):
#     for j in range(5,i,-1):
#         print(" ", end = " ")
#     for k in range (i):
#         print("*", end = " ")
#     print()
# ## Write a program to display this pattern.
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# for i in range(1,6):
#     for j in range(i, 0, -1):
#         print(j, end = " ")
#     print()

# ## Write a program to display this pattern.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range (1,6): ##rows
#     for j in range (1,i+1): ##columns
#         print("*", end = " ") ## iha pe number ke jaygay * pattern de raha, jake * show kare ga
#     print()
# for i in range (5, 0, -1):
#     for k in range (0, i-1):
#         print("*", end =  " ")
#     print()
# ## Write a program to display this pattern.
# Box Pattern
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
# 6 12 18 24 30 36 42 48 54 60
# 7 14 21 28 35 42 49 56 63 70
# 8 16 24 32 40 48 56 64 72 80
# 9 18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100
# for i in range (1, 11):
#     for j in range ( 1, 11):
#         print(i*j, end = " ")
#     print()
# ## Write a program to display this pattern.
# Triangle Pattern
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64
for i in range (1, 9):
    for j in range ( 1, i+1):
        print(i*j, end = " ")
    print()