import sys
from collections import deque

#main 
N, M = map(int, sys.stdin.readline().split())
maze = []
visited = [[False for x in range(M)] for y in range(N)]
route = [[0 for x in range(M)] for y in range(N)]
for n in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

visited[0][0] = True
route[0][0] = 1
x = 0
y = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque([(y, x)])
while q:
    (b, a) = q.popleft()

    for i in range(4):
        if 0 <= b+dy[i] < N and 0 <= a+dx[i] < M and visited[b+dy[i]][a+dx[i]] == False and maze[b+dy[i]][a+dx[i]]==1:
            route[b+dy[i]][a+dx[i]] = route[b][a] + 1
            visited[b+dy[i]][a+dx[i]] = True
            q.append((b+dy[i], a+dx[i]))
                
print(route[N-1][M-1])
