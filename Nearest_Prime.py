from math import sqrt
def isprime(n):
    if(n==1 or n==0):
        return False
    for i in range(2,int(sqrt(n)+1)):
        if(n%i == 0):
            return False
    return True
n = int(input())
for i in range(n):
    a =int(input())
    j,h,g = 1,0,0
    x,y = False,False
    if(isprime(a) == True):
        print(a)
    else:
        while True:
            h = a+j
            g = a-j
            if(isprime(h)== True):
                x = True
            if(isprime(g) == True):
                y = True
            j+=1
            if(x==True or y==True):
                break
        if(x==True and y==True):
            print(g)
        elif(x==True and y==False):
            print(h)
        else:
            print(g)

            
