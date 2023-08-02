n=int(input())
ls=list(map(int,input().split()))
ns=[]
h=n//2
for i in range(n-1,h-1,-1):
    ns.append(ls[i])
for i in range(0,h):
    ns.append(ls[i])
print(*ns)