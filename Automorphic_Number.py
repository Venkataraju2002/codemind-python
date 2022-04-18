n=int(input())
k=n**2
n=str(n)
l1=len(n)
k=str(k)
l2=len(k)
j = k[-l1:]
if(int(j) == int(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    