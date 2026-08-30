import json

with open("students.json", "r") as f:
    data = json.load(f)

    lowest_scorer = ""
    lowest_marks = 100

    for student in data:
        if student["Marks"] < lowest_marks:
            lowest_marks = student["Marks"]
            lowest_scorer = student["Name"]

    print(lowest_scorer)
    print(lowest_marks)

    