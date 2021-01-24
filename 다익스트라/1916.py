import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adL = [[] for y in range(N+1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adL[a].append((b, c)) # to, cost

start, end = map(int, sys.stdin.readline().split())

maxDist = 100000000 # 100000(max dist) * 1000(max nodes)
dist = [maxDist for i in range(N+1)]
check = [False for i in range(N+1)]

dist[start] = 0
for i in range(N-1):
    minDist = maxDist+1
    x = -1
    for j in range(1, N+1):
        if check[j] == False and minDist > dist[j]:
            minDist = dist[j]
            x = j

    check[x] = True
    for k in adL[x]:
        if dist[k[0]] > dist[x] + k[1]:
            dist[k[0]] = dist[x] + k[1]

print(dist[end])
