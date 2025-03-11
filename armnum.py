# Armstrong number

n=int(input("Enter a number:"))
sum,temp=0,n
while temp > 0:
    digit=temp%10
    sum=sum+(digit*digit*digit)
    temp//=10
if sum==n:
    print(n," is an armstrong number")
else:
    print("Not an armstrong number")