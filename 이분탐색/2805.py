import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort(reverse=True)

low = 0
high = (tree[0]-1)*2
mid = 0
maxN = 0
while low <= high:
    mid = (low+high)//2

    n = 0
    for i in tree:
        t = i-mid
        if t >= 0:
            n += t
        if n >= M:
            low = mid+1
            if mid > maxN:
                maxN = mid
            break
    else:
        high = mid-1

print(maxN)
