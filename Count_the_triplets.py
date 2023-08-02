t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    c=0
    for i in ls:
        for j in ls:
            if(i!=j):
                if i+j in ls:
                    c+=1
    if(c>0):
        print(c//2)
    else:
        print(-1)