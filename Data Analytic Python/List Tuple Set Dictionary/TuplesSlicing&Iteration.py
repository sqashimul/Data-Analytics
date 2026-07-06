# Slicing And Iteration in Tuples

##Slicing
a  = ("OnePlus", "Vivo", "Redmi", "Samsung", "Nokia", "Realme", "Nothing", "Apple")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::3])
print(a[1::2])
print(a[::-1])
print(a[2::-1])

##Iteration
b = ("OnePlus", "Vivo", "Redmi", "Samsung", "Nokia", "Realme", "Nothing", "Apple")
##with for loop
for i in b:
    print(i)
## along with range and length in for loop
for i in range(len(b)):
    # print(i)
    print(b[i])
## While Loop
## along with while loop
i = 0
while i < len(b):
    print(b[i])
    i+=1