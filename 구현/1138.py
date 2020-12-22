from itertools import permutations

N = int(input())
left = input()
leftN = left.split()
leftNum = list(map(int, leftN)) # [int x for x in leftN]
answer = ()

for per in permutations(range(1, N+1), N):
    for num in per:
        small = 0
        for i in range(per.index(num)):
            if per[i] > num:
                small += 1
                
        if small != leftNum[num-1]:
            break;
    else:
        answer = per

for a in answer:
    print(str(a), end = ' ')
