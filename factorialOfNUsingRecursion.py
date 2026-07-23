def cal_fact(n):
    if n == 0 or n == 1:
        return 1

    return cal_fact(n-1) * n

print(cal_fact(5))