import re

def solution(new_id):
    # 1단계
    answer = new_id.lower()
    
    # 2단계
    answer = re.sub("[^\w\-\.]", "", answer) # answer이 바뀌는 것이 아니라 바뀐 문자열을 리턴
    
    # 3단계
    answer = re.sub("\.+", ".", answer)

    # 4단계
    answer = re.sub("^\.|\.$", "", answer)    
    
    # 5단계
    if answer == "":
        answer = "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub("^\.|\.$", "", answer)
        
    # 7단계
    length = len(answer) 
    if length <= 2:
        answer += answer[length-1] * (3 - length)
    
    return answer
