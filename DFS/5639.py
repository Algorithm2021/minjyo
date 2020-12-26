import sys
sys.setrecursionlimit(10**5)

def postOrder(start, end):
    if start > end:
        return

    divide = end+1
    for i in range(start+1, end+1): # node[start] is root node
        if nodes[start] < nodes[i]:
            divide = i
            break

    postOrder(start+1, divide-1) # left
    postOrder(divide, end) # right
    print(nodes[start]) # root


nodes = []
while True:
    try:
        v = int(sys.stdin.readline())
    except:
        break

    nodes.append(v)

postOrder(0, len(nodes)-1)
