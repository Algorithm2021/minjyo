import sys
from collections import deque
    
M, N = map(int, sys.stdin.readline().split())
t = []
for n in range(N):
    t.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque([])
day = [[-1 for x in range(M)] for y in range(N)]
for n in range(N):
    for m in range(M):
##        print(n, m)
        if t[n][m] == 1:
            day[n][m] = 0
            q.append((n, m))            

while q:
        (b, a) = q.popleft()

        for i in range(4):
            if 0 <= b+dy[i] < N and 0 <= a+dx[i] < M and t[b+dy[i]][a+dx[i]] == 0 and day[b+dy[i]][a+dx[i]] == -1: # tomato exist and not visited?
                day[b+dy[i]][a+dx[i]] = day[b][a] + 1
                q.append((b+dy[i], a+dx[i]))

result = max(map(max, day))
for n in range(N):
    for m in range(M):
        if t[n][m] == 0 and day[n][m] == -1:
            result = -1

print(result)
