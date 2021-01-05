import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(M)]
result2 = []

numbers.sort()

def backtracking(index, n, m):
    if index == m:
        result2.append(tuple(result))
        return

    for i in numbers:
        result[index] = i
        backtracking(index+1, n, m)

        #after
        result[index]= 0
    
backtracking(0, N, M)

result2 = list(set(result2))
result2.sort()
for i in result2:
    print(*i, sep=' ')
