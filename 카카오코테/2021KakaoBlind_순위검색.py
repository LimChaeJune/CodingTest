def dfs(y,query,graph):
    result = True

    if query[y] == '-':
        result =  True
    elif y == (len(query) -1):
        result = int(graph[y]) >= int(query[y])
    elif graph[y] != query[y]:
        result = False    

    if(result == False):
        return False

    elif (y < len(query) - 1):
        result = dfs(y+1, query, graph)

    return result

    
def createcases(people):
    cases = {}    
    return dict

def solution(info,query):
    answer = []

    peoples = []
    for myInfo in info:
        peoples.append(list(str(myInfo).split()))
        
    for qu in query:
        thisQuery = list(str(qu).replace('and','').split())                

        cnt = 0
        for p in peoples:            
            if dfs(0, thisQuery, p):
                cnt +=1

        answer.append(cnt)

    answer.sort()  
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210", 
"python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250","- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])
