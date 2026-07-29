with open("Practice.txt", "r") as f:
    data = f.read()

NewData = data.replace("Lauda", "Python")

with open("Practice.txt", "w") as f:
    f.write(NewData)