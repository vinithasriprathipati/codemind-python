n=int(input())
ls=list(map(int,input().split()))
ex=int(input())
mc=max(ls)
ns=[]
for i in ls:
    if i>=mc:
        ns.append('True')
    else:
        if i+ex>=mc:
            ns.append('True')
        else:
            ns.append('False')
print(*ns)