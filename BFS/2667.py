import sys
from collections import deque

def bfs(y, x):
    if visited[y][x] == True:
        return -1
    visited[y][x] = True
    
    if town[y][x] == 1:
        cnt = 1
        q.append((y, x))
        while q:
            (b, a) = q.popleft()

            if b-1 >= 0 and visited[b-1][a] == False and town[b-1][a] == 1:
                cnt += 1
                visited[b-1][a] = True
                q.append((b-1, a))

            if b+1 < N and visited[b+1][a] == False and town[b+1][a] == 1:
                cnt += 1
                visited[b+1][a] = True
                q.append((b+1, a))

            if a-1 >= 0 and visited[b][a-1] == False and town[b][a-1] == 1:
                cnt += 1
                visited[b][a-1] = True
                q.append((b, a-1))

            if a+1 < N and visited[b][a+1] == False and town[b][a+1] == 1:
                cnt += 1
                visited[b][a+1] = True
                q.append((b, a+1))

        return cnt     

    else:
        return -1

#main        
N = int(sys.stdin.readline())
town = []
for i in range(N):
    town.append(list(map(int,list(sys.stdin.readline().strip()))))

visited = [[False for x in range(N)] for y in range(N)]
result = []
q = deque([])

for y in range(N):
    for x in range(N):
        cnt = bfs(y, x)
        if cnt > 0:
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)
    
