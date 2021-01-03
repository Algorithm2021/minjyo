import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(M)]

numbers.sort()

def backtracking(index, n, m):
    if index == m:
        print(*result, sep=' ')
        return

    for v in numbers:
        result[index] = v
        backtracking(index+1, n, m)

        #after
        result[index] = 0

backtracking(0, N, M)
