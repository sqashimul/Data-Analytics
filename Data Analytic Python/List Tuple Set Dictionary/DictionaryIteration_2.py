#Dictionary Iteration Part 2
#setdefault #update #pop #popitem #clear
Student = {"name": "John", "class":"6th", "roll_no":23}
#setdefault
x = Student.setdefault("roll_no",24)
x = Student.setdefault("roll_no",23)
print(x)

# Create a dictionary
data = {"a": 1, "b": 2, "c": 3}
print("Original:", data)

# 1. update() - Adds or changes data
data.update({"c": 9, "d": 4})
print("After update:", data)

# 2. pop() - Removes a specific key
val = data.pop("b")
print("Popped value:", val)
print("After pop:", data)

# 3. popitem() - Removes the last item #popitem: Removed the last pair ("d", 4).
item = data.popitem()
print("Popped item:", item)
print("After popitem:", data)

# 4. clear() - Deletes everything
data.clear()
print("After clear:", data)
