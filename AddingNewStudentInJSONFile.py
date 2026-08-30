import json

with open("students.json", "r") as f:
    data = json.load(f)

    new_name = input("Enter name:")
    new_age = int(input("Enter age:"))
    new_course = input("Enter course:")
    new_marks = int(input("Enter marks:"))

    if new_marks >= 40:
        new_passed = True
    else:
        new_passed = False

    new_student = {
        "Name": new_name,
        "Age": new_age,
        "Course": new_course,
        "Marks": new_marks,
        "Passed": new_passed
    }

    data.append(new_student)

    with open("students.json", "w") as f:
        json.dump(data, f, indent=1)