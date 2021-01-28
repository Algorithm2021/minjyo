import sys

TC = int(sys.stdin.readline())

for t in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    maxDist = 100000000
    dist = [0 for i in range(N+1)]
    edges = []
    negativeCycle = False

    for m in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, T)) # from to cost
        edges.append((E, S, T)) # road is Bidirectional
    for w in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, -T)) # from to cost

    for n in range(1, N+1):
        for m in range(2*M+W): # Bidirectional road + Wormhole
            s = edges[m][0]
            e = edges[m][1]
            t = edges[m][2]

            if dist[s] != maxDist and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

                if n == N:
                    negativeCycle = True

    if negativeCycle:
        print("YES")
    else:
        print("NO")
