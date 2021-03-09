import sys

T = int(sys.stdin.readline())
memo = [[0, 0] for i in range(41)]
memo[0] = [1, 0]
memo[1] = [0, 1]

# memozation
for i in range(2, 41):
    memo[i][0] = memo[i-2][0] + memo[i-1][0]
    memo[i][1] = memo[i-2][1] + memo[i-1][1]
    
for t in range(T):
    N = int(sys.stdin.readline())
            
    print(memo[N][0], memo[N][1])
