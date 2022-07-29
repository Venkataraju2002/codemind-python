n=int(input())
l=list(map(int,input().split()))
k=set(l)
k=list(k)
c=0
for i in k:
    if l.count(i)==i:
        c+=1
print(c)