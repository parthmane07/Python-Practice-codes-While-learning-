import json

with open("students.json", "r") as f:
    data = json.load(f)

    find = input("Enter student name:")
    found = False

    for student in data:
        if student["Name"] == find:
            found = True
            new_marks = int(input("Enter new marks:"))
            student["Marks"] = new_marks

            if new_marks >= 40:
                student["Passed"] = True
            else:
                student["Passed"] = False

    if not found:
        print("Student not found")

    with open("students.json", "w") as f:
        json.dump(data, f)