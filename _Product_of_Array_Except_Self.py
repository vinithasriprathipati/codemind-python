n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in range(n):
    pro=1
    for j in range(n):
        if i!=j:
            pro*=ls[j]
    ns.append(pro)
print(*ns)