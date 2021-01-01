import sys

N, K = map(int, sys.stdin.readline().split())

if N >= K:
    print(N-K)
    for i in range(N, K-1, -1):
        print(i, end=' ')
    
else:
    t = [-1 for i in range(K*2)] 
    q = [(-1, N)] #prev, cur
    t[N] = 0
    
    index = 0
    prev = -1
    while True:    
        p, c = q[index]
        left = c-1
        right = c+1
        tp = c*2
    
        if left == K or right == K or tp == K:
            print(t[c]+1)
            prev = c
            break
       
        if 0 <= left < K*2 and t[left] == -1:
            t[left] = t[c]+1
            q.append((c, left))
        if 0 <= right < K*2 and t[right] == -1:
            t[right] = t[c]+1
            q.append((c, right))
        if 0 <= tp < K*2 and t[tp] == -1:
            t[tp] = t[c]+1
            q.append((c, tp))
        index += 1

    result = [K]
    while True:
        if prev == -1:
            break
        (p, c) = (-1, -1)
        for i in q:
            if i[1] == prev:
                (p, c) = i
                result.append(c)
                break
        prev = p

    print(*(reversed(result)), sep=' ')

    # method2
##    def go(n, m):
##    if n != m:
##        go(n, from[m]) # "from[n] = now" in bfs()
##    print(m, end=' ')
##
##    go(n, m)
