import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

A.sort()
for i in num:
    high = len(A)-1
    low = 0
    mid = (high+low)//2
    while low <= high:
        if A[mid] == i:
            print(1)
            break
        elif A[mid] > i:
            high = mid - 1
        elif A[mid] < i:
            low = mid + 1
        mid = (high+low)//2
    else:
        print(0)