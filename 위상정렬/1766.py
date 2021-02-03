import sys
import heapq
##from queue import PriorityQueue -> time error

N, M = map(int, sys.stdin.readline().split())
adL = [[] for i in range(N+1)]
inDegree = [0 for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adL[a].append(b)
    inDegree[b] += 1
    
heap = []
for i in range(1, N+1):
    if inDegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    x = heapq.heappop(heap)
    print(x, end=" ")
    
    for i in adL[x]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
                heapq.heappush(heap, i)
