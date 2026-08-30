import json

with open("students.json", "r") as f:
    data = json.load(f)
    
    find = input("Enter a name:")
    found = False

    for student in data:
        if student["Name"] == find:
            found = True
            data.remove(student)

    if found:
        print("Student removed successfully")
    else:
        print("Student not found")

    with open("students.json", "w") as f:
        json.dump(data, f)