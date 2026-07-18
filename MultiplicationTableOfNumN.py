#1st Method with While loop:
n = int(input("Enter a number :"))

i = 1

while i<=10 :
    print(n*i)
    i=i+1




#2nd Method with For loop:
n = int(input("Enter a number :"))

for i in range(n, (n*10)+1, n):
    print(i)

for i in range(1, 11):
    print(n*i)