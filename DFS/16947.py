import sys
from collections import deque
sys.setrecursionlimit(10**6)

# return -2: cylce exist, not in cycle
# return -1: cylce not exist
# return 1 ~ n: cycle exist, in cycle and start index
def dfs(v, prev):
    if visited[v] == 1: # cycle start index
        return v 
        
    visited[v] = 1

    for i in adL[v]:
        if prev != i:
            result = dfs(i, v)
            
            if result == -2:
                return -2
            if result >= 0:
                visited[v] = 2 # this node is in cycle
                if v == result:
                    return -2 # this node is start index -> next node is not in cycle 
                else:
                    return result
    return -1


N = int(sys.stdin.readline())
adL = [[] for i in range(N)]
visited = [0 for i in range(N)] # 0: not visited, 1: visited, 2: in cycle
d = [-1 for i in range(N)]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    adL[a-1].append(b-1)
    adL[b-1].append(a-1)

dfs(0, -1)

#bfs
q = deque([])
for i in range(N):
    if visited[i] == 2:
        d[i] = 0
        q.append(i)

while q:
    n = q.popleft()

    for i in adL[n]:
        if d[i] == -1:
            d[i] = d[n] + 1
            q.append(i)

for i in d:
    print(i, end=' ')

##print(*d, sep=' ') -> unpacking
