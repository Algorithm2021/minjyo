import sys

N, M = map(int, sys.stdin.readline().split())
b = []
y1 = -1
x1 = -1
y2 = -1
x2 = -1
c = 1
for y in range(N):
    line = list(sys.stdin.readline().strip())
    b.append(line)

    for i, v in enumerate(line):
        if v=='o' and c==2:
            y2 = y
            x2 = i
            break
        if v=='o' and c==1:
            y1 = y
            x1 = i
            c = 2
            
result = 11
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def backtracking(y1, x1, y2, x2, cnt):
    if cnt > 10:
        return
    
    c1 = False
    c2 = False
    if y1 < 0 or y1 > N-1 or x1 < 0 or x1 > M-1:
        c1 = True
    if y2 < 0 or y2 > N-1 or x2 < 0 or x2 > M-1:
        c2 = True

    if c1 and c2:
        return
    if c1 or c2:
        global result
        result = min(result, cnt)
        return

    for i in range(4):
        ny1 = y1+dy[i]
        nx1 = x1+dx[i]
        ny2 = y2+dy[i]
        nx2 = x2+dx[i]

        if 0 <= ny1 < N and 0 <= nx1 < M and b[ny1][nx1] == '#':
            ny1 = y1
            nx1 = x1
        if 0 <= ny2 < N and 0 <= nx2 < M and b[ny2][nx2] == '#':
            ny2 = y2
            nx2 = x2

        backtracking(ny1, nx1, ny2, nx2, cnt+1)
        
backtracking(y1, x1, y2, x2, 0)
if result > 10:
    result = -1
print(result)
