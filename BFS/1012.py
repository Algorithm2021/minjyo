import sys
from collections import deque

def bfs(y, x):
    visited[y][x] = True

    q = deque([(y, x)])
    while q:
        b, a = q.popleft()

        for i in range(4):
            ny = b+dy[i]
            nx = a+dx[i]

            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False and m[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = True

T = int(sys.stdin.readline())
for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    m = [[0 for x in range(M)] for y in range(N)]
    visited = [[False for x in range(M)] for y in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        m[y][x] = 1

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    result = 0
    for y in range(N):
        for x in range(M):
            if m[y][x] == 1 and visited[y][x] == False:
                result += 1
                bfs(y, x)

    print(result)
