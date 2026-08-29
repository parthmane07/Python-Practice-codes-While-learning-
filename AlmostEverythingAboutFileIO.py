with open("students.txt", "r") as f:
    data = f.readlines()

    total_student = 0
    total_marks = 0
    passed_student = 0
    failed_student = 0
    highest_marks = 0
    lowest_marks = 100
    highest_scorer = ""
    lowest_scorer = ""

    with open("result.txt", "w") as f:
        for line in data:
            name, marks = line.split(",")
            marks = float(marks)
            total_student += 1
            total_marks += marks

            if marks > highest_marks:
                highest_marks = marks
                highest_scorer = name

            if marks < lowest_marks:
                lowest_marks = marks
                lowest_scorer = name

            if marks >= 40:
                result = "pass"
                passed_student += 1
            else:
                result = "fail"
                failed_student += 1

            if marks >= 90:
                grade = "A+"
            elif 89 >= marks >= 80:
                grade = "A"
            elif 79 >= marks >= 70:
                grade = "B"
            elif 69 >= marks >= 60:
                grade = "C"
            elif 59 >= marks >= 50:
                grade = "D"
            else:
                grade = "F"

            f.write(str(name) + "--" + str(marks) + " " + result + " " + grade + "\n")

        avg = total_marks/total_student

    with open("result.txt", "a") as f:
        f.write("Total student:" + str(total_student) + "\n")
        f.write("Passed :" + str(passed_student) + "\n")
        f.write("Failed:" + str(failed_student) + "\n")
        f.write("Highest:" + str(highest_scorer) + " " + str(highest_marks) + "\n")
        f.write("Lowest:" + str(lowest_scorer) + " " + str(lowest_marks) + "\n")
        f.write("Average:" + str(avg))