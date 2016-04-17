def prime(n):
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
    return True

total=0
for i in range(2,2000000):
    if prime(i):
        total+=i

print(total)
