a=1
b=1
c=998
while True:
    if a**2+b**2==c**2:
        break
    else:
        if b==c or b==c-1:
            a=a+1
            b=a
        else:
            b=b+1
        c=1000-a-b

print(a*b*c)
