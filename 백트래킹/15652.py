import sys

N, M = map(int, sys.stdin.readline().split())
result = [0 for i in range(M)]

# method 1
def backtracking(index, n, m):
    if index == m:
        print(*result, sep=' ')
        return

    for i in range(1, n+1):
        if result[index-1] <= i or index==0:
            result[index] = i
            backtracking(index+1, n, m)

            #after
            result[index] = 0

backtracking(0, N, M)

# method 2 - order
def backtracking(index, start, n, m):
    if index == m:
        print(*result, sep=' ')
        return

    for i in range(start, n+1): # select number [start ~ N]
        result[index] = i
        backtracking(index+1, i, n, m) # next num is bigger than now 

        #after
        result[index] = 0

backtracking(0, 1, N, M)

# method 3 - select
cnt = [0 for i in range(N+1)]
def backtracking(num, selected, n, m):
    if selected == m:
        for index, value in enumerate(cnt[1:]):
            for i in range(value):
                print(index+1, end=' ')
        print()
        return
    if num > n: # any num is selected
        return

    # num is selected
    for i in range(m-selected, 0, -1): 
        cnt[num] = i # num is selected N times
        backtracking(num+1, selected+i, n, m)
    
    # num is not selected
    cnt[num] = 0
    backtracking(num+1, selected, n, m)

backtracking(1, 0, N, M)


