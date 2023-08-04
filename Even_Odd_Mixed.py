n=int(input())
ec=0
oc=0
mc=0
while(n>0):
    r=n%10
    n//=10
    if r%2==0:
        ec+=1
    else:
        oc+=1
if ec==0:
    print('Odd')
elif oc==0:
    print('Even')
else:
    print('Mixed')