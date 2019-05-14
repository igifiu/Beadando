def hatvany():
    a=int(input('Give a number between 1 and 1million: '))
    while a>1000000:
        print('Give a smaller number')
        a=int(input('Give a number between 1 and 1 million: '))
    h=0; b=0; c=0
    while True:
        b=0
        c=0
        b+=a**h
        c+=a**(h-1)
        h+=1
        if b>1000000:
            break
    return c

print(hatvany())
