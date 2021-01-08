import sys

N = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))

def backtracking(w):
    n = len(w)

    if n == 2: # left, right
        return 0
    
    result = 0
    for i in range(1, n-1):
        r = w[i-1] * w[i+1]
        temp = w[:i] + w[i+1:] # remove i
        r += backtracking(temp)
        if result < r:
            result = r
    return result
        
print(backtracking(w))
