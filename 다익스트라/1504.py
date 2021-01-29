import sys
from queue import PriorityQueue

N, E = map(int,sys.stdin.readline().split())
adL = [[] for y in range(N+1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adL[a].append((b, c)) # to, cost
    adL[b].append((a, c))
v1, v2 = map(int,sys.stdin.readline().split())
    

maxDist = 100000000 # 100000(max dist) * 1000(max nodes)

##check = [False for i in range(N+1)]
##start = 1
##end = v1

def find(start, end):
    q = PriorityQueue()
    dist = [maxDist for i in range(N+1)]
    dist[start] = 0
    q.put((0, start))
    while q.empty()==False:
        x = q.get()[1]
    ##    if check[x] == True:
    ##        continue

    ##    check[x] = True
        for k in adL[x]:
            if dist[k[0]] > dist[x] + k[1]:
                dist[k[0]] = dist[x] + k[1]
                q.put((dist[k[0]], k[0]))

    return dist[end]

result = min(find(1, v1) + find(v1, v2) + find(v2, N), find(1, v2) + find(v2, v1) + find(v1, N))
if result >= maxDist:
    print("-1")
else:
    print(result)
