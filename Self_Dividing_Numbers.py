def self_divide(n):
    s=n
    k=str(n)
    count=0
    while n:
        d=n%10
        n=n//10
        if d==0:
            continue

        if s%d==0:
            count=count+1
            
    if(count==len(k)):
        return True
    return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(self_divide(i)==True):
        print(i,end=" ")



