import json

with open("students.json", "r") as f:
    data = json.load(f)

    passed_student = list()

    for student in data:
        if student["Passed"]:
            passed_student.append(student)

    data_of_passed_student = json.dumps(passed_student)

    print(data_of_passed_student)