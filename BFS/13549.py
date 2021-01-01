import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

if N >= K:
    print(N-K)
else:
    t = [-1 for i in range(K*2)]
    q = deque([N])
    t[N] = 0 

    while q:
        n = q.popleft()
    
        left = n-1
        right = n+1
        tp = n*2
    
        if tp == K:
            print(t[n])
            break
        if left == K or right == K:
            print(t[n]+1)
            break
        
        if 0 <= tp < K*2 and t[tp] == -1: # tp should be first 
            t[tp] = t[n]                  # because tp == right or tp == left
            q.appendleft(tp)              # time(tp) < time(right or left) 

        if 0 <= right < K*2 and t[right] == -1:
            t[right] = t[n]+1
            q.append(right)

        if 0 <= left < K*2 and t[left] == -1:
            t[left] = t[n]+1
            q.append(left)
