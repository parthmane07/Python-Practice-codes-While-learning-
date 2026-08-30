import json

with open("students.json", "r") as f:
    data = json.load(f)

    search = input("Enter a name:")
    found = False
    for student in data:
        if search == student["Name"]:
            found = True
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])

    if found == False:
        print("Student not found")