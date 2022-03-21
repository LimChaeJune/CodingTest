from collections import defaultdict

def solution(record):
    answer = []        
    myDic = defaultdict(str)
        
    result = []
    for value in record:
        values = list(value.split(' '))
        
        if len(values) > 2:
            if values[0] == 'Enter':                
                result.append((values[1], 'Enter'))                
            myDic[values[1]] = values[2]            
        else:
            result.append((values[1], 'Change'))
            
    for res in result:
        if res[1] == 'Enter':
            answer.append(myDic[res[0]] + "님이 들어왔습니다.")
        else:
            answer.append(myDic[res[0]] + "님이 나갔습니다.")
    
    
    return answer