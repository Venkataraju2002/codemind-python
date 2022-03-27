    
def factorial(d):
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    return fact
n=int(input())
s=0
k=n
while n:
    d=n%10
    s=s+factorial(d)
    n=n//10
    
if s==k:
    print("The number", k, "is a strong number")
else:
    print("The number",k, "is not a strong number")


    