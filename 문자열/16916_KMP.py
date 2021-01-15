import sys

def preprocessing(p):
    m = len(p)
    pi = [-1 for i in range(m)]
    pi[0] = 0
    j = 0;
    for i in range(1, m):
        while j>0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            pi[i] = j+1
            j += 1
        else:
            pi[i] = 0

    return pi

def kmp(s, p):
    pi =  preprocessing(p)
    ans = []
    n = len(s)
    m = len(p)
    i = 0
    j = 0
    for i in range(n):
        while j>0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans.append(i-m+1)
                j = pi[j]
            else:
                j += 1
    return ans

s = list(sys.stdin.readline().strip())
p = list(sys.stdin.readline().strip())

matched = kmp(s, p)
if len(matched)>0:
    print(1)
else:
    print(0)
