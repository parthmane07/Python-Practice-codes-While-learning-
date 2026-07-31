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

sum = 0

for i in numbers:
    sum += i

print(sum)