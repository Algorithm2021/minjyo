zeroSum = oneSum = 0

def solution(arr):
    compress(arr, 0, 0, len(arr))
    
    return [zeroSum, oneSum]

def compress(arr, y, x, w):
    global zeroSum, oneSum
    
    if w == 1:
        if arr[y][x] == 0:
            zeroSum += 1
        else:
            oneSum += 1
        return  
    
    cur = arr[y][x]
    can = True
    for i in range(y, y+w):
        for j in range(x, x+w):
            if cur != arr[i][j]:
                can = False
                break
    
    if can:
        if cur == 0:
            zeroSum += 1
        else:
            oneSum += 1
        return
    
    compress(arr, y, x, w//2)
    compress(arr, y, x+w//2, w//2)
    compress(arr, y+w//2, x, w//2)
    compress(arr, y+w//2, x+w//2, w//2)
