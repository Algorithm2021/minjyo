import sys

N, M = map(int, sys.stdin.readline().split())
result = [0 for i in range(M)]

def backtracking(index, n, m):
    if index == m:
        print(*result, sep=' ')
        return

    for i in range(1, n+1):
        result[index] = i
        backtracking(index+1, n, m)
        #after
        result[index] = 0

backtracking(0, N, M)
