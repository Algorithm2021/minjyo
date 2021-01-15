import sys

trie = []

class Node:
    def __init__(self):
        self.children = [-1 for i in range(26)]
        self.valid = False

def init():
    global trie
    x = Node()
    trie.append(x)
    return len(trie)-1

def add(node, s, index):
    global trie
    if index == len(s)-1:
        trie[node].valid = True
        return
    
    c = ord(s[index]) - ord('a')
##    print(node, c, s, index)
    if trie[node].children[c] == -1:
        n = init()
        trie[node].children[c] = n

    child = trie[node].children[c]
    add(child, s, index+1)

def search(node, s, index):
    global trie
    if node == -1:
        return False
    if index == len(s)-1:
        return trie[node].valid

    c = ord(s[index]) - ord('a')
    child = trie[node].children[c]
    return search(child, s, index+1)

N, M = map(int, sys.stdin.readline().split())
root = init()

for i in range(N):
    s = sys.stdin.readline()
    add(root, s, 0)

cnt = 0    
for i in range(M):
    s = sys.stdin.readline()
    if search(root, s, 0) == True:
        cnt += 1

print(cnt)
