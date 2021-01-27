import sys

N, M = map(int, sys.stdin.readline().split())
E = []
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    E.append((a, b, c)) # from to cost
maxDist = 100000000
dist = [maxDist for i in range(N+1)]

dist[1] = 0
negativeCycle = False
for i in range(1, N+1):
    for j in range(M):
        f = E[j][0]
        t = E[j][1]
        c = E[j][2]
        if dist[f] != maxDist and dist[t] > dist[f] + c:
            dist[t] = dist[f] + c
            if i == N:
                negativeCycle = True

if negativeCycle:
    print("-1")
else:
    for i in range(2, N+1):
        if dist[i] == maxDist:
            dist[i] = -1
        print(dist[i])
