def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        print(i)
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if not(sum in answer):
                answer.append(sum)
            
    answer.sort()
    
    return answer
