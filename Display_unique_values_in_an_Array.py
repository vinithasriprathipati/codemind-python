n=int(input())
ls=list(map(int,input().split()))
b=[]
for i in ls:
    c=ls.count(i)
    if c==1:
        b.append(i)
if len(b)!=0:
    print(*b)
else:
    print(-1)