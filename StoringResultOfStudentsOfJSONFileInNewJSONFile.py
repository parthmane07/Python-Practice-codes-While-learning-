import json

with open("students.json", "r") as f:
    data = json.load(f)

    result_list = list()

    for student in data:
        if student["Passed"]:
            result = "Pass"
        else:
            result = "Fail"

        if student["Marks"] >= 90:
            grade = "A"
        elif student["Marks"] >= 75:
            grade = "B"
        elif student["Marks"] >= 60:
            grade = "C"
        elif student["Marks"] >= 40:
            grade = "D"
        else:
            grade = "F"

        individual_student = {
            "name" : student["Name"],
            "marks" : student["Marks"],
            "result" : result,
            "grade" : grade
            }

        result_list.append(individual_student)

    with open("result.json", "w") as f:
        json.dump(result_list, f, indent=4)