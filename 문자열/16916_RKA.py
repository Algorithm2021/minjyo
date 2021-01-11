import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()

mod = 2147483647
base = 256

def h(s):
    result = 0
    for i in s:
        result = (result * base + ord(i)) % mod
    return result

n = len(S)
m = len(P)
if n < m:
    print(0)
    sys.exit(0)

hash_p = h(P)
hash_s = h(S[0:m])

first = 1
for i in range(m-1):
    first = (first * base) % mod

for i in range(n-m+1):
    if hash_p == hash_s:
        print(1)
        sys.exit(0)
    if i+m < n:
        hash_s = hash_s - (ord(S[i]) * first) % mod
        hash_s = (hash_s + mod) % mod
        hash_s = ((hash_s * base) % mod + ord(S[i+m])) % mod
print(0)
