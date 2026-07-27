def count_digits(n):
    count = 0
    while n != 0:
        count += 1
        n = n // 10

    return count

print(count_digits(123456789))