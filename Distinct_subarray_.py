l=int(input())
r=int(input())
s=0
for i in range(l,r+1):
    su=0
    for j in range(i,r+1):
        su+=j
        if(su%2!=0):
            s+=1
print(s)