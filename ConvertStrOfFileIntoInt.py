with open("number.txt", "r") as f:
    data = f.read()
    print(data)

num = ""
numbers = []
for i in range(len(data)):
    if data[i] == ",":
        numbers.append(int(num))
        num = ""
    else:
        num += data[i]

numbers.append(int(num))

print(numbers)
print(type(numbers))