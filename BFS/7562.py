import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
    I = int(sys.stdin.readline())
    y1, x1 = map(int, sys.stdin.readline().split())
    y2, x2 = map(int, sys.stdin.readline().split())

    m = [[-1 for x in range(I)] for y in range(I)]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    m[y1][x1] = 0
    q = deque([(y1, x1)])

    while q:
        b, a = q.popleft()

        for i in range(8):
            ny = b+dy[i]
            nx = a+dx[i]
            if 0 <= ny < I and 0 <= nx < I and m[ny][nx] == -1:
                m[ny][nx] = m[b][a] + 1
                q.append((ny, nx))
            if ny == y2 and nx == x2: # resolve time error
                q = deque([])
                break

    print(m[y2][x2])
