n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    if ls.count(i)==i:
        if i not in ns:
            ns.append(i)
if ns==[]:
    print(-1)
else:
    print(*ns)