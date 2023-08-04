n=int(input())
ls=list(map(int,input().split()))
k=int(input())
ns=[]
for i in ls:
    if ls.count(i)==k:
        ns.append(i)
if ns==[]:
    print(-1)
else:
    print(*set(ns))