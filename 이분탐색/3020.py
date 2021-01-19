import sys

N, H = map(int, sys.stdin.readline().split())
up = []
down = []
for i in range(N):
    if i%2 == 0:
        down.append(int(sys.stdin.readline()))
    else:
        up.append(int(sys.stdin.readline()))
up.sort()
down.sort()

def count(l, h): # count (x >= h) in list
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] < h:
            low = mid+1
        else:
            high = mid-1
    return len(l)-(high+1)

result = N-1
cnt = 0
for i in range(1, H+1):
    Sum = count(down, i) + count(up, H-i+1)
    if Sum < result:
        result = Sum
        cnt = 0
    if Sum == result:
        cnt += 1
        
print(result, cnt)
