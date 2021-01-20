import sys

N = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
w.sort()

low = 0
high = N-1
ans = (w[low] + w[high], 0, 0)

while low < high:
    mid = w[low] + w[high]

    if abs(mid) <= abs(ans[0]):
        ans = (mid, low, high)
        if mid == 0:
            break
        
    if mid < 0: # - > +
        low += 1 # go to 0
    else: # - < +
        high -= 1 # go to 0
        
print(w[ans[1]], w[ans[2]])
