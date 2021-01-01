import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

if M == 1 and N == 1:
    print(0)
    sys.exit(0)
    
m = []
for y in range(N):
    m.append(list(map(int, list(sys.stdin.readline().strip()))))

w = [[-1 for x in range(M)] for y in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = -1
q = deque([(0, 0)])
w[0][0] = 0
while q:
    b, a = q.popleft()

    for i in range(4):
        ny = b+dy[i]
        nx = a+dx[i]

        if 0 <= ny < N and 0 <= nx < M:
##            if ny == N-1 and nx == M-1:
##               if result > w[b][a] or result == -1:
##                result = w[b][a]
                
            if m[ny][nx] == 0 and w[ny][nx] == -1:
                w[ny][nx] = w[b][a]
                q.appendleft((ny, nx))

            if m[ny][nx] == 1 and w[ny][nx] == -1:
                w[ny][nx] = w[b][a] + 1
                q.append((ny, nx))
                
##print(result)
print(w[N-1][M-1])
