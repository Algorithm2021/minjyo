import sys

trie = []

class Node:
    def __init__(self):
        self.children = [-1 for i in range(10)]
        self.valid = False

def init():
    x = Node()
    trie.append(x)
    return len(trie)-1

def add(node, s, index):
    if index == len(s)-1:
        trie[node].valid = True
        return
    
    c = ord(s[index]) - ord('0')
    if trie[node].children[c] == -1:
        n = init()
        trie[node].children[c] = n

    child = trie[node].children[c]
    add(child, s, index+1)

def check(node):
    for i in range(10):
        if trie[node].children[i] != -1:
            if trie[node].valid == True:
                return False
            else:
                if check(trie[node].children[i]) == False:
                    return False
    return True

t = int(sys.stdin.readline().strip())
for i in range(t):
    trie = []
    root = init()
    n = int(sys.stdin.readline().strip())
    
    for j in range(n):
        s = sys.stdin.readline()
        add(root, s, 0)

    if check(root) == True:
        print("YES")
    else:
        print("NO")
