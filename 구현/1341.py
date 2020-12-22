from fractions import Fraction

Input = list(map(int, input().split()))
x = Fraction(Input[0], Input[1])
y = 1-x
##print(y)
if x==0: #only y eat
    print('-')
else:
    n = x/y # pattern legnth >= 2 and must include x, y

    swap = False
    if n<1: # x eat < y eat
        n = 1/n
        temp = x
        x = y
        y = temp
        swap = True
        
    pattern = '*'
    totalX = x - Fraction(1, 2)
    x = Fraction(1, 2)
    y = 0

    i = 1
    while len(pattern)<=59:   
        i += 1
        cake = Fraction(1, 2**i)
        if cake <= totalX:
            x += cake
            totalX -= cake
            pattern += '*'
##            print("x ", cake)
##            print(pattern)
        else:
            y += cake
            pattern += '-'
##            print("y", y)
##            print(pattern)
        if (y!=0 and x/y==n):
            break; 
    else:
        pattern = ''


    if pattern=='':
        print('-1')
    else:
       if swap:
           for i in pattern:
               if i=='*':
                   print('-', end='')
               else:
                   print('*', end='')
       else:
            print(pattern)
