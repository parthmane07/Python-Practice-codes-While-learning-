with open("students.txt", "r") as f:
    data = f.readlines()

    total_student = 0
    total_marks = 0
    highest_student_name = ""
    highest_student_marks = 0
    lowest_student_name = ""
    lowest_student_marks = 100
    passed_student = 0
    failed_student = 0

    for line in data:
        name, marks = line.split(",")
        marks = float(marks)
        total_student += 1
        total_marks += marks

        if marks >= 40:
            passed_student += 1
        else:
            failed_student += 1

        if marks > highest_student_marks:
            highest_student_marks = marks
            highest_student_name = name

        if marks < lowest_student_marks:
            lowest_student_marks = marks
            lowest_student_name = name
            
        avg = total_marks/total_student
        

with open("report.txt", "w") as f:
    f.write("Total Students:" + str(total_student) + "\n")
    f.write("Average marks:" + str(avg) + "\n")
    f.write("Highest:" + str(highest_student_name) + " " + str(highest_student_marks) + "\n")
    f.write("Lowest:" + str(lowest_student_name) + " " + str(lowest_student_marks) + "\n")
    f.write("Passed:" + str(passed_student) + "\n")
    f.write("Failed:" + str(failed_student) + "\n")