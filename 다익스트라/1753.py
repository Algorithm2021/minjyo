import sys
from queue import PriorityQueue

V, E = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())

adL = [[] for y in range(V+1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adL[a].append((b, c)) # to, cost

maxDist = 100000000 # 100000(max dist) * 1000(max nodes)
dist = [maxDist for i in range(V+1)]
check = [False for i in range(V+1)]
q = PriorityQueue()

dist[start] = 0
q.put((0, start))
while q.empty()==False:
    x = q.get()[1]
    if check[x] == True:
        continue

    check[x] = True
    for k in adL[x]:
        if dist[k[0]] > dist[x] + k[1]:
            dist[k[0]] = dist[x] + k[1]
            q.put((dist[k[0]], k[0]))

for i in range(1, V+1):
    if dist[i] >= maxDist:
        print("INF")
    else:
        print(dist[i])
