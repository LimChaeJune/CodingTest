def getStr(val):
    if val == 'zero':
        return 0
    elif val == 'one':
        return 1
    elif val == 'two':
        return 2
    elif val == 'three':
        return 3
    elif val == 'four':
        return 4
    elif val == 'five':
        return 5
    elif val == 'six':
        return 6
    elif val == 'seven':
        return 7
    elif val == 'eight':
        return 8
    elif val == 'nine':
        return 9
    else:
        return -1

def solution(s):    
    result = []
    current = ''
    for i in s:        
        if i.isdigit():
            result.append(int(i))
        else:            
            current += i
            strVal = getStr(current)            
            if strVal > -1:
                result.append(strVal)
                current = ''
            
    answer = int("".join(map(str,(result))))
    return answer