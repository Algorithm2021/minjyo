def solution(n):
    answer = []
    triangle = [[0 for j in range(i)] for i in range(1, n+1)]
    maxX = maxY = n-1
    minX = minY = 0
    
    maxN = 0
    for i in range(1, n+1):
        maxN += i
   
    curN = 1
    curX = curY = 0
    triangle[curY][curX] = 1
    
    while curN <= maxN:
        # down
        while curY < maxY:
            curN += 1
            curY += 1
            triangle[curY][curX] = curN
        minX += 1
        minY += 1
        
        if curN >= maxN:
            break
        
        # right
        while curX < maxX:
            curN += 1
            curX += 1
            triangle[curY][curX] = curN
        maxY -= 1
        
        if curN >= maxN:
            break
        
        # up
        while curY > minY:
            curN += 1
            curX -= 1
            curY -= 1
            triangle[curY][curX] = curN
        minY += 1
        maxX -= 2
        
    for t in triangle:
        for i in t:
            answer.append(i)
    
    return answer
