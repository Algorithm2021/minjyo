import sys
from collections import deque

line = list(sys.stdin.readline().strip())
left = deque([])
for i in line:
    left.append(i)
M = int(sys.stdin.readline())
right = deque([])

for m in range(M):
    op = sys.stdin.readline().split()

    if op[0] == 'L':
        if left:
            right.appendleft(left.pop())

    elif op[0] == 'D':
        if right:
            left.append(right.popleft())

    elif op[0] == 'B':
        if left:
            left.pop()

    elif op[0] == 'P':
        left.append(op[1])

left.extend(right)
print(*left, sep='')
