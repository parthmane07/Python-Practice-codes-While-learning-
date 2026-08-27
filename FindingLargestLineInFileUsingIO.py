with open("notes.txt", "r") as f:
    data = f.readlines()

lenght = data[0]

for line in data:
    if len(line) > len(lenght):
        lenght = line

print(lenght)
print(len(lenght))