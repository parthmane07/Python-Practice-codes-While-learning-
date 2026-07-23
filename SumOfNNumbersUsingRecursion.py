def SumOfN(n):
    if n == 0:
        return 0 

    return SumOfN(n-1) + n
   

print(SumOfN(5))