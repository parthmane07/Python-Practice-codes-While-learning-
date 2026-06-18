#Calculator

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

print("select operation:")
print("1 for add")
print("2 for sub")
print("3 for mul")
print("4 for div")

opp = int(input("Enter the operation: "))

if opp == 1:
    print("result:", num1 + num2)

elif opp == 2:
    print("result:", num1 - num2)

elif opp == 3:
    print("result:", num1 * num2)

elif opp == 4:
    print("result:", num1 / num2)

else:
    print("invalid opperation")