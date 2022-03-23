n=int(input())
a=list(map(int,input().split()))
c=[]
count=0
for i in a:
    if i not in c:
        c.append(i)
for i in c:
    if i%2==0:
        count+=1
print(count)