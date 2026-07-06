## Iteration in Dictionaries
Student = {"name": "John", "class":"6th", "roll_no":23}
print(Student["name"])
#printing all the key names one by one
for x in Student:
    print(x)
#printing all the value names one by one
for x in Student:
    print(Student[x])
#using value function
for x in Student.values(): ##Use this function
    print(x)
#using items function
for x,y in Student.items():
    # print(x,y)
    print(x, ":", y)
