with open("students.txt", "r") as f:
    data = f.readlines()

    passed = 0
    failed = 0
    for line in data:
        name, marks = line.split(",")
        marks = float(marks)

        if marks >= 40:
            passed += 1
        else:
            failed += 1

    print("Passed:", passed)
    print("Failed:", failed)