import sys

def main():
    sys.setrecursionlimit(20000)
    
    K = int(sys.stdin.readline())
    
    for i in range(K):
        V, E = map(int, sys.stdin.readline().split())
        adL = [[] for x in range(V+1)]
        visit = [0 for x in range(V+1)] # 0: not visited, 1: visited g1, 2: visited g2

        for e in range(E):
            a, b = map(int, sys.stdin.readline().split())
            adL[a].append(b)
            adL[b].append(a)

        for v in range(V):
            if visit[v] == 0:
                dfs(adL, visit, v, 1)

        flag = False
        for v in range(V):
            if flag == True:
                break
            for a in adL[v]:
                if visit[v]==visit[a]:
                    print('NO')
                    flag = True
                    break
        else:
            print('YES')

        adL = []
        visit = []


def dfs(adL, visit, v, c):
    visit[v] = c

    for i in adL[v]:
        if visit[i] == 0:
            dfs(adL, visit, i, 3-c) # g1 -> g2, g2 -> g1

main()
