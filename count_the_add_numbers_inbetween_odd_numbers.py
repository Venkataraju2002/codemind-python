n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)-2):
    if (l[i]%2==l[i+2]%2) and l[i+1]%2==1:
        c+=1
print(c)
        