import sys
from collections import deque

def bfs(y, x, group):
    g[y][x] = group
    d[y][x] = 0
    bfs_q.append((y, x))

    q = deque([(y, x)])
    while q:
        b, a = q.popleft()
        
        for i in range(4):
            ny = b+dy[i]
            nx = a+dx[i]

            if 0 <= ny < N and 0 <= nx < N and g[ny][nx] == 0 and m[ny][nx] == 1:
                    q.append((ny, nx))
                    g[ny][nx] = group
                    d[ny][nx] = 0
                    bfs_q.append((ny, nx))
    
N = int(sys.stdin.readline())
m = []
for i in range(N):
    m.append(list(map(int, sys.stdin.readline().split())))

g = [[0 for x in range(N)] for y in range(N)]
d = [[-1 for x in range(N)] for y in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

group = 1
bfs_q = deque([])
for y in range(N):
    for x in range(N):
        if g[y][x] == 0 and m[y][x] == 1:
            bfs(y, x, group)
            group += 1

while bfs_q:
        b, a = bfs_q.popleft()

        for i in range(4):
            ny = b+dy[i]
            nx = a+dx[i]

            if 0 <= ny < N and 0 <= nx < N and d[ny][nx] == -1:
                    d[ny][nx] = d[b][a] + 1
                    g[ny][nx] = g[b][a]
                    bfs_q.append((ny, nx))

result = -1 # N is not max result
for y in range(N):
    for x in range(N):
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < N and 0 <= nx < N and g[ny][nx] != g[y][x]: # adjacent group
                if result > d[ny][nx] + d[y][x] or result == -1:
                    result = d[ny][nx] + d[y][x]
            
print(result)
