##       Json Problem Solving
""" 1. Convert the following dictionary into JSON format.
  Student_data = {"Name":"David", "age":13, "marks": 87}
  2. Access the value of age from the given data.
   Student_data = {"Name":"David", "age":13, "marks": 87}
  3.Pretty Print following JSON data.
   Student_data = {"Name":"David", "age":13, "marks": 87} 
  4. Sort the following JSON keys and write them into a file.
   Student_data = {"Name":"David", "age":13, "marks": 87}
 $ 5. Access the nested key marks from the following nested data
 """
# import json

#   """{"student":{
#         "grade":{
#            "name":"David"
#                "marks":{
#                   "math":87,}
#     }
# } """
##1. Convert the following dictionary into JSON format.
#import json
# Student_data = {"Name":"David", "age":13, "marks": 87}
# print(type(Student_data))
# data = json.dumps(Student_data)
# print(data)
# print(type(data))
##2. Access the value of age from the given data.
# import json
# Student_data = '{"Name":"David", "age":13, "marks": 87}'
#
# data = json.loads(Student_data)
# print(data["age"])
## 3.Pretty Print following JSON data.
# Student_data = {"Name":"David", "age":13, "marks": 87}
# data = json.dumps(Student_data, indent=4, separators=(",", "="))
# print(data)
##4. Sort the following JSON keys and write them into a file.
# Student_data = {"Name":"David", "age":13, "marks": 87}
# f = open("demo.json", "w")
# data = json.dumps(Student_data, indent=4, short_key = True)
# f.write(data)
# print("The data has been added to the file")
## 5. Access the nested key marks from the following nested data

import json

# Added three closing curly braces to complete the JSON object
import json

# Inserted the mark inside the nested "marks" object
student_data = """{ "student":{
                    "grade":{
                        "name":"David", 
                        "marks":{
                            "score": 87
                        }
                    }
                  }
               }"""

data = json.loads(student_data)
print(data["student"]["grade"]["marks"])


