i = 100
while i != 0:
    r = 0
    if i % 2 == 0:
        i = i/2
    elif i % 2 == 1:
        r = 1
        i = (i - 1) / 2
    if r == 0:
        print(0, end='')
    else:
        print(1, end='')

        

