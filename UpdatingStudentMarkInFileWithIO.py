with open("students.txt", "r") as f:
    data = f.readlines()

found = False
remaining = []

search = input("Enter student name: ")
new_mark = input("Enter new marks: ")

for line in data:
    name, mark = line.split(",")

    if search == name:
        remaining.append(name + "," + new_mark + "\n")
        found = True
    else:
        remaining.append(line)

if found == False:
    print("Student not found")
else:
    with open("students.txt", "w") as f:
        f.writelines(remaining)