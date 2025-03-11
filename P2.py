# 2.Check prime number

n=int(input("Enter the number:"))
flag = 0

for i in range(2, n//2 + 1):
    if n % i == 0:
        flag = 1
        break

if flag == 0 and n > 1:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
