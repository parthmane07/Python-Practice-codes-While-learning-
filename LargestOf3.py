num1 = int(input("Enter 1st num:"))
num2 = int(input("Enter 2nd num:"))
num3 = int(input("Enter 3rd num:"))

if (num1 >= num2 and num1 >= num3):
    print(num1, "is the largest.")

elif (num2 >= num1 and num2 >= num3):
    print(num2, "is the largest.")

else:
    print(num3, "is the largest.")