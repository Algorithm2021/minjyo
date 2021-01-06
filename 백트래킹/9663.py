import sys
from collections import deque

N = int(sys.stdin.readline())
board = [[-1 for x in range(N)] for y in range(N)] # -1: not visited, 0: visited but can't, 1: can
cnt = 0

def backtracking(y, result, q):
    if y==N:
        global cnt
        cnt += 1
        return

    for i in range(N):
        for j in range(y):
            if result[j] == i or (abs(j-y)==abs(result[j]-i)):
                break
        else:
            result[y] = i
            backtracking(y+1, result, q)
        

for x in range(N):
    result = [-1 for y in range(N)] # result[i] = j -> q in (i, j)
    result[0] = x # every column has queen!
    backtracking(1, result, 1)

print(cnt)
