with open("students.txt", "r") as f:
    data = f.readlines()

    total = 0
    count = 0
    for line in data:
        name, marks = line.split(",")
        total += float(marks)
        count += 1

    print(total)
    avg = total/count
    print(avg)