n=int(input())
ls=list(map(int,input().split()))
tc=0
for i in ls:
    c=0
    while(i>0):
        rem=i%10
        c+=1
        i=i//10
    if c%2==0:
        tc+=1
print(tc)