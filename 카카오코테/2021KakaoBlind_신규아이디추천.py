def solution(newid):
    import re

    answer = ''
    newid = str(newid).lower()    

    for id in newid:
        if id.isalnum() or id in '-_.':
            answer += id
            

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    answer = 'a' if len(answer) == 0 else answer
    
    
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer [-1] == '.' :
            answer = answer[:-1]    
    
    if len(answer) <= 2:
        answer = answer + answer[-1] * (3- len(answer))

    return answer
solution(input())