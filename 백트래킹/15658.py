import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split())) # + - x ÷
maxSum = -10**9
minSum = 10**9

def backtracking(ops, op0, op1, op2, op3, selected):
    if selected == N-1:
        result = num[0]
        for i, v in enumerate(ops):
            if v == 0:
                result += num[i+1]
            elif v == 1:
                result -= num[i+1]
            elif v == 2:
                result *= num[i+1]
            else:
                if result >= 0:
                    result //= num[i+1]
                else:
                    result = -((-result)//num[i+1])
      
        global maxSum, minSum
        maxSum = max(result, maxSum)
        minSum = min(result, minSum)
        return
                
    if op0 > 0:
        temp = ops[:] # copy
        temp.append(0)
        backtracking(temp, op0-1, op1, op2, op3, selected+1)

    if op1 > 0:
        temp = ops[:] # copy
        temp.append(1)
        backtracking(temp, op0, op1-1, op2, op3, selected+1)

    if op2 > 0:
        temp = ops[:] # copy
        temp.append(2)
        backtracking(temp, op0, op1, op2-1, op3, selected+1)

    if op3 > 0:
        temp = ops[:] # copy
        temp.append(3)
        backtracking(temp, op0, op1, op2, op3-1, selected+1)
    
backtracking([], op[0], op[1], op[2], op[3], 0)


print(maxSum)
print(minSum)
