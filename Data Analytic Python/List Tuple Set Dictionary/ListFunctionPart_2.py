## List Python Functions Part (2)
a = ["Thor", "Hulk", "Ironman", "Captain America"]
## to create a copy of a list
b = []
print(b)
b = a.copy()
print(b)
## to access an element
print(a.index("Ironman"))
print(a.index("Thor"))
## to entend the list
c = ["Vision", "Spiderman"]
a.extend(c)
print(a)
## to reverse the list
a.reverse()
print(a)
## to sort the list
d = [1, 7, 8, 5, 15, 2, 30]
d.sort()
print(d)
a.sort()
print(a)
## to clear all the data from the list
a.clear()
print(a)
d.clear()
print(d)
