def solution(n):
    answer = 0
    list = []
    
    while(n!=0):
        list.append(n%3)
        n = n//3
    
    list.reverse()
    
    for i in range(len(list)):
        answer += (3**i)*list[i]  

    return answer
