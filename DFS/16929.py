import sys

def dfs(y, x, cnt, color):
    if visited[y][x] == True:
        if (cnt - d[y][x]) >= 4: # cycle length >= 4
            return True
        else:
            return False
        
    visited[y][x] = True
    d[y][x] = cnt
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < M:
            if g[ny][nx] == color:
                if dfs(ny, nx, cnt+1, color):
                    return True
    return False
               
        
N, M = map(int, sys.stdin.readline().split())
visited = [[False for x in range(M)] for y in range(N)]
d = [[0 for x in range(M)] for y in range(N)]
g = []
for n in range(N):
    g.append(list(sys.stdin.readline().strip()))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for n in range(N):
    for m in range(M):
        if visited[n][m] == False:
            if dfs(n, m, 0, g[n][m]):
                print('Yes')
                sys.exit(0)
    
print('No')
