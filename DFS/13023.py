import sys

N,M = map(int, sys.stdin.readline().split())

adM = [[False for i in range(N)] for j in range(N)]
adL = [[] for i in range(N)]
edges = []

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    
    edges.append((a,b))
    edges.append((b,a))
    
    adM[a][b] = True
    adM[b][a] = True

    adL[a].append(b)
    adL[b].append(a)

for i in range(2*M): # relation is Bidirectional -> 2M edges
    for j in range(2*M):
        # a->b
        a = edges[i][0]
        b = edges[i][1]

        # c->d
        c = edges[j][0]
        d = edges[j][1]

        if a==b or a==c or a==d or b==c or b==d or c==d: # same person exist?
            continue

        # b->c
        if not adM[b][c]: 
            continue

        # d->e
        for E in adL[d]:
            if E==a or E==b or E==c:
                continue
            print(1)
            sys.exit(0)
            
else:
    print(0)
