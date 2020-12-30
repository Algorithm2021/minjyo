import sys
from collections import deque
    
N = int(sys.stdin.readline())
adL = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if b != 1: # 1 visited
        adL[a].append(b)
    if a != 1: # 1 visited
        adL[b].append(a)
line = list(map(int, sys.stdin.readline().split()))

if line[0]!=1: # start is always 1
    print(0)
    sys.exit(0)
    
q = deque([])
for k in line[1:1+len(adL[1])]:
    if k not in adL[1]:
        print(0)
        sys.exit(0)
    else:
        q.append(k)

        for j in adL[k]:
            adL[j].remove(k) # visited

i = 1+len(adL[1])        
while q:
    n = q.popleft()
    if i < len(line):
        if i+len(adL[n]) > len(line):
            print(0)
            sys.exit(0)
        for k in line[i:i+len(adL[n])]:
            if k not in adL[n]:
                print(0)
                sys.exit(0)
            else:
                q.append(k)

                for j in adL[k]:
                    adL[j].remove(k) # visited
        i = i+len(adL[n])
    else:
        break 

print(1)
