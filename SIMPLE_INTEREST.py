p,r,t=map(int,input().split())
a=p*(pow((1+r/100),t))
si=(p*r*t//100)
print(si)