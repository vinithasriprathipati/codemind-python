import math
n=int(input())
ls=list(map(int,input().split()))
print(math.lcm(*ls))