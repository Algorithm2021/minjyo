import sys

def main():
    sys.setrecursionlimit(10**6)
    
    N, M = map(int, sys.stdin.readline().split())
    visit = [False for x in range(N+1)]
    adL = [[] for x in range(N+1)]
    
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adL[u].append(v)
        adL[v].append(u)

    c = 0
    for i in range(1, N+1):
        if visit[i]==False:
            dfs(adL, visit, i)
            c += 1
    print(c)

def dfs(adL, visit, v):
    visit[v] = True

    for i in adL[v]:
        if visit[i]==False:
            dfs(adL, visit, i)

main()
