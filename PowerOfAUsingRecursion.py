def power(a, n):
    if n == 1:
        return a

    return power(a, n-1) * a
        

print(power(10, 2))

