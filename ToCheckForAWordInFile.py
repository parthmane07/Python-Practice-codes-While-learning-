with open("Practice.txt", "r") as f:
    data = f.read()

result = data.find("learning")

if result != -1:
    print("FOUND")
else:
    print("NOT FOUND")