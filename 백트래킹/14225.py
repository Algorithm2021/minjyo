import sys

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
S.sort()
result = [False for i in range(sum(S)+1)]

def backtracking(i, cur, N, S, result):
    if i == N:
        result[cur] = True
        return

    # not selected
    backtracking(i+1, cur, N, S, result)
    
    # selected
    cur += S[i]
    backtracking(i+1, cur, N, S, result)

  
backtracking(0, 0, N, S, result)

for i in range(1, len(result)):
    if result[i] == False:
        print(i)
        break
else:
    print(len(result))
