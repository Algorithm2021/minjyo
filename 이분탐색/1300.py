import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

low = 1
high = k # Knd num <= k
ans = 0
while low <= high:
    mid = (low+high)//2  

    cnt = 0
    for i in range(1, N+1):
        temp = mid//i
        if temp < 0:
            break
        cnt += min(temp, N) # temp can not more than N

    if cnt >= k:
        ans = mid
        high = mid-1
    else:
        low = mid+1
    
print(ans)             
