import sys

def main():    
    N = int(sys.stdin.readline())
    adL = [[] for x in range(N+1)]
    visit = [False for x in range(N+1)]
    global cnt
    cnt = -1 #except node 1

    k = int(sys.stdin.readline())
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        adL[a].append(b)
        adL[b].append(a)

    dfs(adL, visit, 1)
    print(cnt)

def dfs(adL, visit, v):
    visit[v] = True
    global cnt
    cnt += 1
    
    for i in adL[v]:
        if visit[i] == False:
            dfs(adL, visit, i)
            
main()
