n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    if ls.count(i)==1:
        if i>=s:
            s=i
if(s==0):
    print(-1)
else:
    print(s)
        
