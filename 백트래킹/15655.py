import sys

N, M = map(int, sys.stdin.readline().split())
check = [False for i in range(N+1)]
numbers = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(M)]

numbers.sort()

# select
def backtracking(index, selected, n, m):
    if selected == m:
        print(*result, sep=' ')
        return

    if index == n: # any num is selected
        return

    # num is selected
    result[selected] = numbers[index]
    backtracking(index+1, selected+1, n, m)

    # num is not selected
    result[selected] = 0
    backtracking(index+1, selected, n, m)
    

backtracking(0, 0, N, M)
