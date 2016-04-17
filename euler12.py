def divisor(n):
    num=1
    for i in range(2,int(n**0.5)):
        if n%i==0:
            num+=1
    num*=2
    if n**0.5==int(n**0.5):
        num+=1
    return num

i=1
term=1
while divisor(term)<=500:
    i+=1
    term+=i

print(term)
