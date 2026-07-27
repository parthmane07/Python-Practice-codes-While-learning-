def IsPalindrom(n):
    reverse = 0
    num = n
    while n != 0:
        x = n % 10
        reverse = (reverse * 10) + x
        n = n // 10

    if num == reverse:
        return True
    else:
        return False


print(IsPalindrom(909))