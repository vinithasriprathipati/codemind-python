n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    ns.append(i*i)
ns.sort()
print(*ns)