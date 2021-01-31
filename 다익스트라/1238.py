import sys
from queue import PriorityQueue

N, M, X = map(int, sys.stdin.readline().split())
adL = [[] for i in range(N+1)]
for i in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    adL[s].append((e, t)) # to cost
check = [False for i in range(N+1)]
maxDist = 1000000000
dist1 = [maxDist for i in range(N+1)] # from X
dist2 = [maxDist for i in range(N+1)] # to X


def find(dist, X, adL):
    q = PriorityQueue()
    dist[X] = 0
    q.put((0, X)) # dist(priority), node
    while q.empty()==False:
        x = q.get()[1]
        if check[x] == True:
            continue

        check[x] = True
        for k in adL[x]:
            if dist[k[0]] > dist[x]+k[1]:
                dist[k[0]] = dist[x]+k[1]
                q.put((dist[k[0]], k[0]))
    return dist

dist1 = find(dist1, X, adL)

check = [False for i in range(N+1)]
adL2 = [[] for i in range(N+1)] # reverse graph
k = 1
for i in adL[1:]:
    for j in i:
        adL2[j[0]].append((k, j[1]))
    k += 1
dist2 = find(dist2, X, adL2)

dist = [x+y for x,y in zip(dist1, dist2)]
print(max(dist[1:]))
