import sys
from collections import deque

def bfs(y, x, c):
    visited[y][x] = True

    q = deque([(y, x)])
    while q:
        (b, a) = q.popleft()

        for i in range(4):
            ny = b + dy[i]
            nx = a + dx[i]

            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == False and p[ny][nx] == c:
                visited[ny][nx] = True
                q.append((ny, nx))
        
    
N = int(sys.stdin.readline())
visited = [[False for x in range(N)] for y in range(N)]
p = []
for n in range(N):
    p.append(list(sys.stdin.readline().strip()))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = 0
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            result += 1
            bfs(y, x, p[y][x])
print(result, end=' ')

result = 0
visited = [[False for x in range(N)] for y in range(N)]
for y in range(N):
    for x in range(N):
        if p[y][x] == 'G':
            p[y][x] = 'R'
            
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            result += 1
            bfs(y, x, p[y][x])
print(result)
