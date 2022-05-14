n=input()

c=[]
for i in n:
    if i.isalpha()==True:
        c.append(i.lower())
p=set(c)
l=list(p)
l.sort()
if len(l)==len(n):
    print("True")
else:
    print("False")