import sys

N = int(sys.stdin.readline())

number = [['###', '#.#', '#.#', '#.#', '###'], #0
          ['..#', '..#', '..#', '..#', '..#'], #1
          ['###', '..#', '###', '#..', '###'], #2
          ['###', '..#', '###', '..#', '###'], #3
          ['#.#', '#.#', '###', '..#', '..#'], #4
          ['###', '#..', '###', '..#', '###'], #5
          ['###', '#..', '###', '#.#', '###'], #6
          ['###', '..#', '..#', '..#', '..#'], #7
          ['###', '#.#', '###', '#.#', '###'], #8
          ['###', '#.#', '###', '..#', '###'], #9
          ]

info = [] #input
avail = [] #available numbers
avg = 0 
for n in range(N):
    info.append([])
    avail.append([])
for i in range(5):
    line = input()
    for n in range(N):
        info[n].append(line[4*n:4*n+3])

cnt = [0]*N #number of avail numbers at each digit
for n in range(N):
    for index, num in enumerate(number):
        for i, s in enumerate(num):
            if s[0]=='.' and info[n][i][0]=='#':
                break;
            if s[1]=='.' and info[n][i][1]=='#':
                break;
            if s[2]=='.' and info[n][i][2]=='#':
                break;
        else:
            avail[n].append(index)
            cnt[n] += 1

    if avail[n]==[]:
        avail=[[]]
        break;

if avail==[[]]:
    print(-1)
else:
    num = 1 #number of avail numbers 
    for n in range(N):
        num *= cnt[n]
        
    for n in range(N):
        for i in avail[n]:
            avg += i*(10**(N-n-1))*(num/cnt[n])

    print(avg/num)
            
############################################## sum of avail numbers (time error) #########################################            
###    print(list(product(*avail)))
##    for p in list(product(*avail)):
##        num = 0
##        for i in range(N):
##            num += p[i] * (10**(N-i-1))
####            print(p)
####            print(num)
##        if num not in avg:
##            avg.append(num)
###    print(avg)
##    if len(avg)==0:
##        print(-1)
##    else:
##        print(sum(avg)/len(avg))
