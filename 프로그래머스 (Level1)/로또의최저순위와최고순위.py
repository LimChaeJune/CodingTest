from copy import deepcopy

def solution(lottos, win_nums):
    answer = []
    topRank = deepcopy(lottos)
    lowRank = deepcopy(lottos)
    
    top_result = 7
    for i in win_nums:
        if i in topRank:
            top_result -= 1
        elif 0 in topRank:            
            for j in range(len(topRank)) :
                if topRank[j] == 0:
                    topRank[j] = i
                    top_result -= 1
    
    if top_result == 7 : top_result = 6
    answer.append(top_result)                
    
    low_result = 7                    
    for i in win_nums:
        if i in lowRank:
            low_result -= 1
    
    if low_result == 7 : low_result = 6
    answer.append(low_result)                
    return answer