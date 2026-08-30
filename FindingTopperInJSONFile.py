import json

with open("students.json", "r") as f:
    data = json.load(f)

    highest_scorer = ""
    highest_marks = 0

    for student in data:
        if student["Marks"] > highest_marks:
            highest_marks = student["Marks"]
            highest_scorer = student["Name"]

    print(highest_scorer)
    print(highest_marks)

    