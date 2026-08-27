with open("students.txt", "r") as f:
    data = f.readlines()

found = False
remaining = []

delete = input("Enter student name: ")

for line in data:
    name, mark = line.split(",")

    if delete == name:
        found = True
    else:
        remaining.append(line)

if found == False:
    print("Student not found")
else:
    with open("students.txt", "w") as f:
        f.writelines(remaining)