n=int(input())
a=list(map(int,input().split()))
x=[]
s=0
c=0
for i in a:
    b=a.count(i)
    if(i==b and i not in x):
        x+=[i]
        c+=1
        s+=i
if(c==0):
    print('-1')
else:
    avg=s/c
    print("%0.2f"%avg)