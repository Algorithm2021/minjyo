import sys

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
cnt = 0

def backtracking(i, result, num, N, S):
    if i == N:
        if result == S:
            global cnt
            cnt += 1
        return
    
    # not selected
    backtracking(i+1, result, num, N, S)
    
    # selected
    result += num[i]
    backtracking(i+1, result, num, N, S)

backtracking(0, 0, num, N, S)
if S == 0:
    print(cnt-1)
else:
    print(cnt)
