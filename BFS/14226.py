import sys
from collections import deque

S = int(sys.stdin.readline())
t = [[-1 for i in range(S+1)] for j in range(S+1)]
t[1][0] = 0

q = deque([(1, 0)]) # S, clipboard
while q:
    s, c = q.popleft() # divide vertex by clipboard num

    if t[s][s] == -1: # not visited
        t[s][s] = t[s][c] + 1
        q.append((s, s)) # copy

    if s+c <= S and t[s][s+c] == -1:
        t[s+c][c] = t[s][c] + 1
        q.append((s+c, c)) # paste

    if s-1 >= 0 and t[s-1][c] == -1:
        t[s-1][c] = t[s][c] + 1
        q.append((s-1, c)) # delete

result = -1
for i in range(S):
    if t[S][i] != -1:
        if result > t[S][i] or result == -1:
            result = t[S][i]

print(result)
