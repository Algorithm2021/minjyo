from itertools import combinations

def solution(orders, course):
    answer = []
    menus = {} # key: 메뉴 개수, value: { key: 메뉴 조합, value: 메뉴 주문 횟수}
    
    for order in orders:
        for c in course:
            for comb in combinations(sorted(order), c):
                if c not in menus:
                    menus[c] = {}
                menu = "".join(comb)
                if menu not in menus[c]:
                    menus[c][menu] = 0
                menus[c][menu] += 1

    for c in course:
        if c in menus:
            m = max(menus[c].values())

            if m >= 2: # 2명 이상 주문한 조합일 때
                answer.extend([k for k, v in menus[c].items() if menus[c][k] == m])
        
    return sorted(answer)
