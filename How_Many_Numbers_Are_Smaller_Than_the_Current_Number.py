n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    c=0
    for j in ls:
        if j<i:
            c+=1
    ns.append(c)
print(*ns)