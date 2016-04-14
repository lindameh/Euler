def palindrome(n):
    a=n
    b=0
    while a!=0:
        b=b*10+a%10
        a=a//10
    if b==n:
        return True
    else:
        return False

def product(n):
    factor=999
    while factor>=100 and n//factor<=999:
        if n%factor==0:
            return True
        factor-=1
    return False
 
max=999999
while True:
    if palindrome(max):
        if product(max):
            print(max)
            break
    max-=1
