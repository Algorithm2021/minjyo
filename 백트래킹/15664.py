import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(M)]
result2 = []

numbers.sort()

def backtracking(index, selected, n, m):
    if selected == m:
        result2.append(tuple(result))
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

result2 = list(set(result2))
result2.sort()
for i in result2:
    print(*i, sep=' ')
