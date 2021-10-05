def solution(n, s, a, b, fares):
    answer = 0
    maxDist = 20000000 # 200(최대 지점 갯수) * 100000(최대 요금)
    dist = [[maxDist for _ in range(n+1)] for _ in range(n+1)] # dist[i][j] i에서 j까지 이동하는데 최소 비용
    
    for fare in fares:
        dist[fare[0]][fare[1]] = fare[2]
        dist[fare[1]][fare[0]] = fare[2]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    answer = 40000000 # 원래 maxDist * 방문해야 하는 지점이 2개 
    for k in range(1, n+1):
        if answer > dist[s][k] + dist[k][a] + dist[k][b]:
            answer = dist[s][k] + dist[k][a] + dist[k][b]
        
    return answer
