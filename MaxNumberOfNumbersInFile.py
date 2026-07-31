with open("number.txt", "r") as f:
    data = f.read()

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

i = 0
max = 0
while i < len(numbers):
    if numbers[i] > max :
        max = numbers[i]
    i += 1

print(max)