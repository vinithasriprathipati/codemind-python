n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ns=[]
for i in range(n):
    ns.append(a[i]+b[i])
print(*ns)