import sys
from collections import deque

N = int(sys.stdin.readline())
adL = [[] for i in range(N+1)]
inDegree = [0 for i in range(N+1)] # prev nodes of i 
work = [0 for i in range(N+1)]
time = [0 for i in range(N+1)] # time until node finished
for i in range(1, N+1):
    line = list(map(int, sys.stdin.readline().split()))
    work[i] = line[0]
    for j in line[2:]:
        adL[j].append(i) 
        inDegree[i] += 1

q = deque([])
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)
        time[i] = work[i]
     
while q:
    x = q.popleft()

    for i in adL[x]:
        inDegree[i] -= 1
        if time[i] < time[x] + work[i]: # x -> i
            time[i] = time[x] + work[i]
        if inDegree[i] == 0:
            q.append(i)

# last node from q can not be max time node
result = 0
for i in time:
    if result < i:
        result = i
        
print(result)
