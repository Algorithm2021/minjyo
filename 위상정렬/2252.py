import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
adL = [[] for i in range(N+1)]
inDegree = [0 for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adL[a].append(b)
    inDegree[b] += 1
    
q = deque([])
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=" ")
    
    for i in adL[x]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)
