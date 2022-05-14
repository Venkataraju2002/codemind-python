n=input()
k=input()
c,d=[],[]
for i in n:
    c.append(i.lower())
for i in k:
    d.append(i.lower())
c1=c.copy()
c2=d.copy()
c1.sort()
c2.sort()
if c!=d and c1==c2:
    print("True")
else:
    print("False")