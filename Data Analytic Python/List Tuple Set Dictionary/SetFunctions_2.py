# Set Python Functions Part 2
#isdisjoint #issubset #issuperset #update #clear
a = {"Ironman", "Hulk", "Thor", "Captain America"}
b = {"Superman", "Batman", "Wonder-Woman"}
c = {"Hulk", "Thor"}
# c = {"Hulk", "Thor", "Spiderman"}

#isdisjoint
print(a.isdisjoint(b)) # Here is no element in set a
print(a.isdisjoint(c)) # Here is element in set a
#issubset
print(a.issubset(b)) # Here is no element in set b
print(c.issubset(a)) # Here is element in set a [Hulk, Thor]

#issuperset
print(a.issuperset(b)) # Here "b" element in set a, or not in a
print(b.issuperset(a)) # Here "a" element in set b, or not in b
print(a.issuperset(c)) # Here "c" element in set a, or not in a
print(b.issuperset(c)) # Here "c" element in set b, or not in b

#update
a.update(c) # Only came to unique value like "Spiderman"
print(a)

#clear
a.clear()
print(a)

x = {1,2,3,4,5}
y = {6,7,8}
z = {1,2}
# z = {1,2,9}
#isdisjoint
print(x.isdisjoint(y)) # Here is no element in set x
print(x.isdisjoint(z)) # Here is element in set x
# #issubset
print(x.issubset(y)) # Here is no element in set b
print(z.issubset(x)) # Here is element in set x {1, 2}
print(x.issubset(z)) # Here is element in set x {1, 2}

#issuperset
print(x.issuperset(y)) # Here "y" element in set x, or not in x
print(y.issuperset(x)) # Here "x" element in set y, or not in y
print(x.issuperset(z)) # Here "z" element in set x, or not in x
print(y.issuperset(z)) # Here "z" element in set y, or not in y

#update
x.update(z) # Only came to unique value like "Spiderman"
print(x)

#clear
x.clear()
print(x)
