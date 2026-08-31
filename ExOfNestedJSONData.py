import json

with open("college.json", "r") as f:
    data = json.load(f)

    print(data["college"])
    print(data["location"])

    highest_scorer_name = ""
    highest_scorer_course = ""
    highest_marks = 0

    for i in data["students"]:
        if i["Marks"] > highest_marks:
            highest_scorer_name = i["Name"]
            highest_scorer_course = i["Course"]
            highest_marks = i["Marks"]
            
    print(highest_scorer_name)
    print(highest_scorer_course)
    print(highest_marks)