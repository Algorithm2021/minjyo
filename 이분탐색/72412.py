from itertools import combinations

def lowerBound(data, target): # 찾고자 하는 값보다 크거나 같은 원소가 처음 나오는 인덱스
    start = 0
    end = len(data) - 1
    mid = (start + end) // 2
    
    while start < end:
        if target <= data[mid]:
            end = mid
        else:
            start = mid + 1
        mid = (start + end) // 2
            
    return start

def solution(info, query):
    answer = []
    
    apply = {} # key: (언어)+(직군)+(경력)+(소울푸드), value: [해당 조건을 만족하는 지원자의 점수]
    for i in info:
        s = i.split()
        tags = s[:-1]

        for i in range(5): # 조건 4개 중에서 0~4개 선택하는 경우의 수 -> 16가지
            for comb in combinations(tags, i):
                tag = ''.join(comb) 
                if tag not in apply:
                    apply[tag] = []
                apply[tag].append(int(s[4])) 
    
    for key in apply.keys(): 
        apply[key] = sorted(apply[key]) # 그룹마다 점수로 지원자 정보 오름차순 정렬
    
    for q in query:
        arr = q.split()
        cond = ""
        for i, a in enumerate(arr):
            if i % 2 == 0 and a != '-':
                cond += arr[i]    
        
        if cond not in apply: # 딕셔너리에 키가 없다 == 원하는 조건의 지원자가 아무도 없었다.
            answer.append(0)
            continue
            
        k = lowerBound(apply[cond], int(arr[-1]))
        if apply[cond][k] < int(arr[-1]): # 조건은 맞지만 원하는 점수 이상인 지원자가 없는 경우
            answer.append(0)
        else:
            answer.append(len(apply[cond]) - k)

    return answer
