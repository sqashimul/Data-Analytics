# Set Python Functions Part 1
#add #pop #remove #discard #copy
a = {"Ironman", "Hulk", "Thor", "Captain America"}

#add
a.add("Spiderman") #Here Spiderman add result showing any random place, because set is ont ordered data
print(a)

# #pop
a.pop() #jekono random value is poping
print(a)

#remove
a.remove("Thor") #specific/particular value is remove like "Thor"
print(a)

#discard
a.discard("Hulk")
print(a)

#copy
b = a.copy()
print(b)