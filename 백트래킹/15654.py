import sys

N, M = map(int, sys.stdin.readline().split())
check = [False for i in range(N+1)]
numbers = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(M)]

numbers.sort()

# order
def backtracking(index, n, m):
    if index == m:
        print(*result, sep=' ')
        return

    for i, v in enumerate(numbers):
        if check[i] == False:
            check[i] = True
            result[index] = v
            backtracking(index+1, n, m)

            #after
            check[i] = False
            result[index] = 0

backtracking(0, N, M)
