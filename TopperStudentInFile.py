with open("students.txt", "r") as f:
    data = f.readlines()

    highest_name = ""
    highest_marks = 0

    for line in data:
        name, marks = line.split(",")
        marks = int(marks)

        if marks > highest_marks:
            highest_marks = marks
            highest_name = name

    print(highest_name, highest_marks)