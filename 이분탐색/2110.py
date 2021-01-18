import sys

sys.setrecursionlimit(10**8)

N, C = map(int, sys.stdin.readline().split())
x = []
for i in range(N):
    x.append(int(sys.stdin.readline()))
x.sort()

low = 1 # min dist
high = x[N-1] - x[0] # max dist
result = 0 # max of mids
# low, high, mid is not x[n]. It is distance.
while low <= high:
    mid = (low+high)//2
    prev = x[0]
    cnt = 1

    for i in range(1, N):
        if x[i]-prev >= mid:
            cnt += 1
            prev = x[i]

    if cnt >= C:
        low = mid+1 # up dist
        result = mid
    else:
        high = mid-1 # down dist

print(result)
