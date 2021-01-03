import sys

N, M = map(int, sys.stdin.readline().split())
check = [False for i in range(N+1)]
result = [0 for i in range(M)]

# method 1
def backtracking(index, n, m):
    if index == m:
        print(*result, sep=' ')
        return

    for i in range(1, n+1):
        if check[i] == False:
            if result[index-1] < i or index==0:
                check[i] = True
                result[index] = i
                backtracking(index+1, n, m)

                #after
                check[i] = False
                result[index] = 0

backtracking(0, N, M)

# method 2 - order
def backtracking(index, start, n, m):
    if index == m:
        print(*result, sep=' ')
        return

    for i in range(start, n+1): # select number [start ~ N]
        if check[i] == False:
            check[i] = True
            result[index] = i
            backtracking(index+1, i+1, n, m) # next num is bigger than now 

            #after
            check[i] = False
            result[index] = 0

backtracking(0, 1, N, M)

# method 3 - select
def backtracking(num, selected, n, m):
    if selected == m:
        print(*result, sep=' ')
        return
    if num > n: # any num is selected
        return

    # num is selected
    result[selected] = num
    backtracking(num+1, selected+1, n, m)

    # num is not selected
    result[selected] = 0
    backtracking(num+1, selected, n, m)

backtracking(1, 0, N, M)
