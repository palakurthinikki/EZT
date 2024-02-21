#find duplicate value
'''n=int(input())
L=list(map(int,input().split()))
for i in range(len(L)):
    if(L[i] in L[0:i]):
        print(L[i])
        break'''
#APPROACH 2
'''n=int(input())
L=list(map(int,input().split()))
L.sort()
for i in range (n):
    if L[i]==L[i+1]:
        print(L[i])
        break'''
#approach 3
'''n=int(input())
L=list(map(int,input().split()))[:n]
for i in L:
    c=L.count(i)
    if c > 1:
        print(i)
        break'''
    
#unique number
'''n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
for i in range (n):
    c=a.count(i)
    if c == 1:
        print(i,end=" ")'''

#CUBE GRAVITY
'''n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
for i in range (n):'''
#cooking
'''n=int(input())
for i in range(n):
    d=int(input())
    t1=0
    t2=0
    for j in range(1,d+1):
        if d%j == 0:
            if j%2 == 0:
                t1=t1+1
            else:
                t2=t2+1
    if t1 == t2:
        print(1)
    else:
        print(0)'''
#APPROACH 2
'''n=int(input())
for i in range(n):
    d=int(input())
    factors=[]
    for j in range (1,d+1):
        if d%j == 0:
            factor.append(j)
    ef=0
    of=0
    for j in factor:
        if j%2 == 0:
            ef.append(j)
        else:
            of.append(j)
    if len(ef) == len(Of):
        print(1)
    else:
        print(0)'''
#cost of groceries
'''n,x=map(int,input().split())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
count=0
for i in range(n):
    if b[i]>=x :
        print(count+c[i])'''
#PRIME NUMBER
'''n=int(input())
count=0
if(n%2 == 0):
    print("not prime") 
else:
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count == 2:
        print("prime")
    else:
        print("not prime")'''

#RUNNING
'''a=int(input())
b=int(input())
c=2*a
d=b*b
if(c>d):
    print("alice is happy")
else:
    print("bob is happy")'''
#even perfect no
'''n=int(input())
s=0
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
    s=0'''

           
           
           


            
        
    
        
