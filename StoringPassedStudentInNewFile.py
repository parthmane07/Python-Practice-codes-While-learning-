with open("students.txt", "r") as f:
    data = f.readlines()
    with open("passed_sudents.txt", "w") as f:
        for line in data:
            name, marks = line.split(",")
            marks = float(marks)

            if marks >= 40:
                marks = str(marks)
                f.write(name + "," + marks + "\n")