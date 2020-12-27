import sys
from collections import deque

def bfs(y, x):
    visited[y][x] = True
   
    if m[y][x] == 1:
        dy = [-1, -1, -1, 0, 1, 1, 1, 0]
        dx = [-1, 0, 1, 1, 1, 0, -1, -1]

        q.append((y, x))
        
        global cnt
        cnt += 1
        while q:
            (b, a) = q.popleft()
            
            for i in range(8):
                if (b+dy[i] >=0 and b+dy[i] < h and a+dx[i] >=0 and a+dx[i] < w and
                    visited[b+dy[i]][a+dx[i]] == False and m[b+dy[i]][a+dx[i]] == 1):
                    q.append((b+dy[i], a+dx[i]))
                    visited[b+dy[i]][a+dx[i]] = True
        
#main
w = 0
h = 0
m = []
visited = []
cnt = 0
q = deque([])
while True:
    cnt = 0
    m = []
    q = deque([])

    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    visited = [[False for x in range(w)] for y in range(h)]
    for i in range(h):
        m.append(list(map(int, sys.stdin.readline().split())))
    
    for y in range(h):
        for x in range(w):
            if visited[y][x] == False:
                 bfs(y, x)
    print(cnt)
    
