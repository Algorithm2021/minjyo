def solution(s):
    curStr = s
    zeroSum = 0
    cnt = 0
    
    while curStr != "1":
        curLen = len(curStr)
        zeroCnt = curStr.count("0")
        curLen -= zeroCnt
        zeroSum += zeroCnt
        
        curStr = ""
        while curLen > 0:
            curStr = str(curLen % 2) + curStr
            curLen = curLen // 2 
        
        cnt += 1
        
    return [cnt, zeroSum]
