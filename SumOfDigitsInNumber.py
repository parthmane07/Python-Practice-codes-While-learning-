def SumOfDigit(n):
    sum = 0
    while n != 0:
        temp = n % 10
        sum += temp
        n = n // 10
        temp = 0

    return sum

print(SumOfDigit(12345))