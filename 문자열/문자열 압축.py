def solution(s):        
    answer = 1000
        
    for i in range(1,len(s)+1):        
        prev = s[:i]
        # 현재 idx
        j = i
        # 현재 카운트
        k = 1
        # answerStr
        currentAnswer = ''
        while True:                
            
            if prev != s[j:j+i]:
                if k > 1:
                    currentAnswer += str(k) + prev
                else:
                    currentAnswer += prev     
                k = 1
            else:
                k += 1
                
            prev = s[j:j+i]                        
            
            # 범위가 str 넘어가면 
            if  j + i > len(s):      
                if k > 1:
                    currentAnswer += str(k) + prev
                else:
                    currentAnswer += s[j:]
                break
            else:
                j += i
        
        answer = min(len(currentAnswer), answer)
                    
    return answer

solution('aabbaccc')