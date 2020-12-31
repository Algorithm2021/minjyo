import sys
from collections import deque

N = int(sys.stdin.readline())
adL = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    adL[a].append(b)
    adL[b].append(a)
line = list(map(int, sys.stdin.readline().split()))
visited = [False for i in range(N+1)]
order = [-1 for i in range(N+1)]
for index, value in enumerate(line):
    order[value] = index

for a in adL:
    a.sort(key=lambda x: order[x]) # sort by order[x]
    
dfs_order = []

def dfs(x):
    if visited[x] == True:
        return
    visited[x] = True
    dfs_order.append(x)

    for i in adL[x]:
        dfs(i)

dfs(1)

for i in range(N):
    if dfs_order[i] != line[i]:
        print(0)
        break
else:
    print(1)
