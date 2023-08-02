import math
n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    sq=i**0.5
    t=int(sq)
    if(sq==t):
        ns.append(i)
print(sum(ns))