import json

with open("students.json", "r") as f:
    data = json.load(f)

    total_student = 0
    total_marks = 0

    for student in data:
        total_student += 1
        total_marks += student["Marks"]

    avg = total_marks / total_student
    print("Avg marks:", avg)