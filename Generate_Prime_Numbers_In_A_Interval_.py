from math import sqrt
def isprime(n):
    if(n ==0 or n ==1):
        return False
    for i in range(2,int(sqrt(n)+1)):
        if(n%i == 0):
            return False
    return True        


n = int(input())
m=int(input())
for i in range(n,m+1):
    if isprime(i)==True:
        print(i)