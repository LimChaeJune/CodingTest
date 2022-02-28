from collections import defaultdict

def solution(id_list, report, k):
    reports = set(report)
    
    user_singo_array = defaultdict(set)
    user_singo_num = defaultdict(int)
    
    for i in reports:
        writer, target = i.split()
        
        user_singo_array[writer].add(target)
        user_singo_num[target] += 1        
        
    answer = []
    
    for i in range(len(id_list)):
        userid = id_list[i]
        user_targets = user_singo_array[userid]
        result = 0
        for key, value in user_singo_num.items():            
            if value >= k:
                if key in user_targets:                    
                    result += 1
        
        answer.append(result)                
        
    return answer
