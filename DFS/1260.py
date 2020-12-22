import sys
from collections import deque 

def main():
    N, M, V = map(int, sys.stdin.readline().split())
    adj = [[] for i in range(N+1)]
    visit = [False for i in range(N+1)]
    
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    for i in adj: # pick min num in adj
        i.sort()

    dfs(visit, adj, V)
    visit = [False for i in range(N+1)]
    print()
    bfs(visit, adj, V)

    
def dfs(visit, adj, v):
    visit[v] = True
    print(v, end=' ')
    
    for i in adj[v]:
        if not visit[i]:
            dfs(visit, adj, i)

def bfs(visit, adj, v):
    q = deque([v])
    visit[v] = True
    print(v, end=' ')

    while q:
        x = q.popleft()

        for i in adj[x]:
            if not visit[i]:
                visit[i] = True
                print(i, end=' ')
                q.append(i)
        
main()       
