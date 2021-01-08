import sys    

def backtracking(i, selected, result, num):
    if selected == 6:
        print(*result, sep=' ')
        return
    if i == len(num):
        return

     # selected
    result[selected] = num[i]
    backtracking(i+1, selected+1, result, num)
    
    # not selected
    result[selected] = 0
    backtracking(i+1, selected, result, num)
    
   
    
while True:
    num = list(map(int, sys.stdin.readline().split()))
    k = num[0]
    if k == 0:
        sys.exit(1)
    result = [0 for i in range(6)]

    backtracking(1, 0, result, num)
    print()
