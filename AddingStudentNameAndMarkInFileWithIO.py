with open("students.txt", "a") as f:

    y_n = "y"
    
    while y_n == "y":
        name = input("Enter name:")
        mark = input("Enter mark:")
        f.write(name + "," + mark + "\n")
        y_n = input("Add another student?(y/n)")