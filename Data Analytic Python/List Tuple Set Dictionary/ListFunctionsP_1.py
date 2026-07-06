## List Python Functions
a = ["Thor", "Hulk", "Ironman", "Captain America","Hulk"]
print(a)
## to find the length of a list
print(len(a))
## to count on occurence of a particular element
print(a.count("Hulk"))
## to add to the list
a.append("Spiderman")
print(a)
## to add to a specific location
a.insert(3,"Vision") ## Negative Index can use
print(a)
## to remove from a list
a.remove("Spiderman")
print(a)
## to remove from a certain location
print(a.pop(1))
print(a)

