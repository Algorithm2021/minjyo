Input = list(map(int, input().split()))
r1 = Input[0]
c1 = Input[1]
r2 = Input[2]
c2 = Input[3]
maxAbs = max(abs(r1), abs(c1), abs(r2), abs(c2)) 
rect = [[0]*(c2 - c1 + 1) for i in range(r2 - r1 + 1)] #answer
r = maxAbs #curR
c = maxAbs #curC
#print(rect) 

cur = (2*maxAbs+1)**2 
for i in range(maxAbs+1):
    #left
##    print()
    for j in range(2*maxAbs+1):
##        print('{0} ({1},{2}) '.format(cur, r, c), end=' ')
        if r>=r1 and r<=r2 and c>=c1 and c<=c2:
            rect[r-r1][c-c1] = cur
        cur += -1    
        c += -1
        
    #up
    c += 1
    r += -1
##    print()
    for j in range(2*maxAbs):
##        print('{0} ({1},{2}) '.format(cur, r, c), end=' ')
        if r>=r1 and r<=r2 and c>=c1 and c<=c2:
            rect[r-r1][c-c1] = cur
        cur += -1
        r += -1
    
    #right
    r += 1
    c += 1
##    print()
    for j in range(2*maxAbs):
##        print('{0} ({1},{2}) '.format(cur, r, c), end=' ')
        if r>=r1 and r<=r2 and c>=c1 and c<=c2:
            rect[r-r1][c-c1] = cur
        cur += -1
        c += 1
    
    #down
    c += -1
    r += 1
##    print()
    for j in range(2*maxAbs-1):
##        print('{0} ({1},{2}) '.format(cur, r, c), end=' ')
        if r>=r1 and r<=r2 and c>=c1 and c<=c2:
            rect[r-r1][c-c1] = cur
        cur += -1
        r += 1
        
    r += -1
    c += -1
    maxAbs += -1

maxLen = len(str(max(map(max, rect))))
for i in rect:
    for j in i:
        print(' ' * (maxLen - len(str(j))) + str(j), end=' ')
    print()
