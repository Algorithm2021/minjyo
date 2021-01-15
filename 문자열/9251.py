import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
LCS = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
ans = 0

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
        

print(LCS[-1][-1])
