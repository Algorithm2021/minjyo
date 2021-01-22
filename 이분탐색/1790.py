import sys

N, K = map(int, sys.stdin.readline().split())

def Len(n):
    l = 1
    start = 1
    result = 0
    while start <= n:
        end = start*10-1
        if end > n:
            end = n
        result += (end-start+1)*l
        l += 1
        start *= 10

    return result


if Len(N) < K:
    print("-1")
else:
    low = 1
    high = N
    result = -1
    l = 0
    while low <= high:
        mid = (low+high)//2

        l = Len(mid)

        if l < K:
            low = mid+1
        else:
            result = mid
            high = mid-1

    result = str(result)
    print(result[len(result)-(l-K)-1]);
