N = int(input())
newN = 0
Sum = 0 
cycle = 1 

Sum += N//10
Sum += N%10
newN = (N%10)*10 + Sum%10

while(N!=newN):
    Sum = 0

    Sum += newN//10
    Sum += newN%10   
    newN = (newN%10)*10 + Sum%10

    cycle += 1

print(cycle)