import sys

K, N = map(int, sys.stdin.readline().split())
L = []
for i in range(K):
    L.append(int(sys.stdin.readline()))
L.sort(reverse=True)

low = 0
high = L[0]*2 # can have not used line
maxN = 0
mid = 0
while low <= high:
    mid = (low + high)//2
    
    n = 0
    for l in L:
        n += l//mid
        if n >= N:
            low = mid+1
            if maxN < mid:
                maxN = mid
            break
    else:
        high = mid-1

print(maxN)
