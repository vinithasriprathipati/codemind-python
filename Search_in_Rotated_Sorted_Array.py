n=int(input())
ls=list(map(int,input().split()))
se=int(input())
for i in range(len(ls)):
    if ls[i]==se:
        print(i)
        break
else:
    print(-1)