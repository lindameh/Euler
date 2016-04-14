n=600851475143
i=2
max=0
while n!=1:
    while n%i==0:
        max=i
        n=n//i
    i=i+1

print(max)
