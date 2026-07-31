a = [1,2,3,4,10,55,23,99,88,77]
b = [3,4,5,6,55,10,42,99]
common = []


for i in a:
    for j in b:
        if i == j:
            common.append(i)

print(common)