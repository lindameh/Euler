sum=0
a1=1
a2=2
a3=3
while a1<=4000000:
    if a1%2==0:
        sum+=a1
    a1=a2
    a2=a3
    a3=a1+a2

print(sum)
