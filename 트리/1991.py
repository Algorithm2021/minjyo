import sys

class Node:
    def __init__(self):
        self.left = None
        self.right = None
   
def preOrder(node):
    if node == -1:
        return
    print(chr(node + ord('A')), end='')
    preOrder(tree[node].left)
    preOrder(tree[node].right)

def inOrder(node):
    if node == -1:
        return
    inOrder(tree[node].left)
    print(chr(node + ord('A')), end='')
    inOrder(tree[node].right)
        
def postOrder(node):
    if node == -1:
        return
    postOrder(tree[node].left)
    postOrder(tree[node].right)
    print(chr(node + ord('A')), end='')
        
def main():
    N = int(sys.stdin.readline())
    global tree
    tree = [Node() for x in range(N)]

    for i in range(N):
        node, left, right = sys.stdin.readline().split()
        
        node = ord(node) - ord('A')
        
        if left == '.':
            tree[node].left = -1
        else:
            tree[node].left = ord(left) - ord('A')
        if right == '.':
            tree[node].right = -1
        else:
            tree[node].right = ord(right) - ord('A')
    
    preOrder(0)
    print()
    inOrder(0)
    print()
    postOrder(0)

main()
