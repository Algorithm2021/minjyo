import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(N)]

numbers.sort()

# select
def backtracking(index, selected, n, m):
    if selected == m:
        for index, value in enumerate(result):
            for i in range(value):
                print(numbers[index], end=' ')
        print()
        return

    if index == n: # any num is selected
        return

    # num is selected
    for i in range(m-selected, 0, -1):
        result[index] = i
        backtracking(index+1, selected+i, n, m)

    # num is not selected
    result[index] = 0
    backtracking(index+1, selected, n, m)
    

backtracking(0, 0, N, M)
