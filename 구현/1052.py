#1 =========================== time error =========================================
##Input = list(map(int, str(input()).split()))
##N = Input[0]
##K = Input[1]
##
##shop = 0
##bottles = [1] * N
##
##minWater = 1
##i = 0
##while N!=K:
##    #i = minWater
##    minBottle = [x for x in bottles if x==minWater]
###    print("minBottle: " + str(minBottle))
##
##    if len(minBottle)<2:
##        nextMins = [x for x in bottles if x>minWater]
###        print("nextMins: " + str(nextMins))
##        
##        if not nextMins: # nextMins empty -> minWater == maxValue 
##            shop += 1
##            N += 1
##            bottles.append(1)
##            minWater = 1
###            print("bottles: " + str(bottles))
##        else:
##            minWater = min(nextMins)
##            
##    else:
##        bottles.append(minBottle[0]*2)
##        bottles.remove(minBottle[0])
##        bottles.remove(minBottle[1])
##        N -= 1
###        print("bottles after add: " + str(bottles))
##        
##print(shop)
#1 =============================================================================


#2 =============================================================================
Input = list(map(int, str(input()).split()))
N = Input[0]
K = Input[1]

shop = 0
binary = bin(N)[2:]

if K >= N:
    print(0)
else:
    # must be K >= number of 1 
    while K < binary.count('1'):
        shop += 1
        N += 1
        binary = bin(N)[2:]

    print(shop)
        
