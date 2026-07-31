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
print("Numbers list is: ",numbers)

i = 0
max = numbers[0]
while i < len(numbers):
    if numbers[i] > max :
        max = numbers[i]
    i += 1

CopyOfNumbers = numbers.copy()
CopyOfNumbers.remove(max)

j = 0
Smax = CopyOfNumbers[0]
while j < len(CopyOfNumbers):
    if CopyOfNumbers[j] > Smax :
        Smax = CopyOfNumbers[j]
    j += 1

print("Second laargest:",Smax)

print("Numbers list is: ",numbers)
print("Copy of numbers list is:", CopyOfNumbers)
