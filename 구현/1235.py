from itertools import combinations

N = int(input())
students = []
numbers = []
same = False
length = 0

for i in range(N):
    students.append(input())
    numbers.append('/')
length = len(students[0])

for index in range(length):
    for i, stu in enumerate(students):
        numbers[i] = str(stu[length-index-1]) + str(numbers[i])

    for c in combinations(numbers, 2):
        if(c[0] == c[1]):
            same = True
            break;
    else:
        same = False
    
    if not same:
        print(index+1)
        break;
