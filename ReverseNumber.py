def reverse_number(n):
    reverse = 0
    while n != 0:
        x = n % 10
        reverse = (reverse * 10) + x
        n = n // 10

    return reverse


print(reverse_number(123))