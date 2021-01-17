import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

A.sort()

def binary(low, high, i):
    if low > high:
        return 0
    
    mid = (low + high)//2
    
    if A[mid] == i:
        return A[low:high+1].count(i)
    elif A[mid] > i:
        return binary(low, mid-1, i)
    elif A[mid] < i:
        return binary(mid+1, high, i)

result = {}
for i in num:
    if i not in result:
        result[i] = binary(0, N-1, i)
        
for i in num:
    if i in result:
        print(result[i], end=' ')
    else:
        print('0', end=' ')
