## A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# 1. Write a program to separate the following string into coma(,) separated values.
# 2. Write a program to sort strings alphabetically in python.
# 3. Write a program to remove a given character from string.
## Z = "F.R.I.E.N.D.S."
# 4. Write a program to remove dot(.) from the following string.
# f. Write a program to check the number of occurrence


a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# 1. Write a program to separate the following string into coma(,) separated values.
b = a.split(".")
print(b)

# 2. Write a program to sort strings alphabetically in python.
# a = input("Enter anything here: ")
#
# b = sorted(a)
# print(b)
# 3. Write a program to remove a given character from string.
a = "hello"
b = a.replace("e", "")
print(b)
## Z = "F.R.I.E.N.D.S."
# 4. Write a program to remove dot(.) from the following string.
z = "F.R.I.E.N.D.S."

B = z.replace(".", "")
print(B)
# 5. Write a program to check the number of occurrence

a =  "she sells seashells on the sea shore"
b = a.count("sea")
print("The number of times substring sea is occurring is:", b)