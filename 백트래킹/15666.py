import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(N)]
result2 = []

numbers.sort()

def backtracking(index, selected, n, m):
    if selected == m:
        temp = []
        for i, v in enumerate(result):
            for k in range(v):
                temp.append(numbers[i])
        result2.append(tuple(temp))
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

result2 = list(set(result2))
result2.sort()
for i in result2:
    print(*i, sep=' ')
