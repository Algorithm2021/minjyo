from itertools import combinations

answer = ""
word = input()
newWord = []

for part in combinations(range(1, len(word)),2): # word[:0] is empty list
    newWord.append((word[:part[0]])[::-1] + (word[part[0]:part[1]])[::-1] + (word[part[1]:])[::-1])

answer = newWord[0]
for word in newWord[1:]:
    i = 0
    while word[i] == answer[i]:
        i += 1
        
    if word[i] < answer[i]:
        answer = word
   
print(answer)
