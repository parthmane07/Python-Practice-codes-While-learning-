import json

student = {
    "Name" : "Parth",
    "Age" : 19,
    "Course" : "BCA",
    "Marks" : 90,
    "Passed" : True
    }

with open("student.json", "w") as f:
    json.dump(student, f)