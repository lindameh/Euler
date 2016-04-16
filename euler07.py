count=1
num=2
while count!=10001:
    num+=1
    k=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            k=False
    if k:
        count+=1

print(num)
