n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    if ls.count(i)==i:
        ns.append(i)
if ns==[]:
    print(-1)
else:
    print(min(ns),end=' ')
    print(max(ns))