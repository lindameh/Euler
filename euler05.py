n=20
num=1
for i in range(2,n+1):
    factor=i
    number=num
    for j in range(2,i):
        while number%j==0 and factor%j==0:
            number//=j
            factor//=j
    num*=factor

print(num)
