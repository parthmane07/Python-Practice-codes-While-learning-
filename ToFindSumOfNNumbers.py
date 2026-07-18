#Using While:
n = int(input("Enter a num:"))
i = 1
x = 0

while i <= n:
    x = x + i
    i += 1

print(x)


#Using For:
n = int(input("Enter a num:"))
sum = 0

for i in range(n+1):
    sum = sum + i
    i += 1

print(sum)