import heapq

def dijkstra(s, n, edge):
    visited = [False for _ in range(n+1)] # 해당 지점을 방문했는가 
    maxDist = 20000000 # 200(최대 지점 갯수) * 100000(최대 요금)
    dist = [maxDist for _ in range(n+1)] # 해당 지점에 대한 최소 요금
    
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    
    while q:
        v = heapq.heappop(q)
        x = v[1]
        
        if visited[x] == True: 
            continue
        visited[x] = True
        
        for k in edge[x]:
            if dist[k[0]] > dist[x] + k[1]: # 현재 저장된 k에 가는데 드는 비용 > x에 가는데 드는 비용 + x에서 k로 가는데 드는 비용   
                dist[k[0]] = dist[x] + k[1]
                heapq.heappush(q, (dist[k[0]], k[0]))
    
    return dist
    
def solution(n, s, a, b, fares):
    answer = 0
    edge = [[] for _ in range(n+1)] # 간선별 요금 정보 저장 edge[출발지점] = [(도착지점, 요금)]  
    maxDist = 20000000 # 200(최대 지점 갯수) * 100000(최대 요금)
    
    for fare in fares:
        edge[fare[0]].append((fare[1], fare[2]))
        edge[fare[1]].append((fare[0], fare[2]))
    
    startDist = dijkstra(s, n, edge)
    answer = startDist[a] + startDist[b] # (S -> A) + (S -> B) 합승하지 않는 경우
    
    for i in range(1, n+1):
        if i != s and startDist[i] < maxDist:
            nDist = dijkstra(i, n, edge) # 합승 -> A, B 최단 경로 요금 / 어떤 특정 지점을 시작 지점이라고 보고 다시 최단 경로를 찾는다.
            if answer > startDist[i] + nDist[a] + nDist[b]:
                answer = startDist[i] + nDist[a] + nDist[b] 
    
    return answer
