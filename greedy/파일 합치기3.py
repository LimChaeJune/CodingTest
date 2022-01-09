T = int(input())

for i in range(T):
    pageCnt = int(input())
    result = 0
    
    items = list(map(int,input().split()))        

    while(True):        
        sumList = []

        if len(items) % 2 == 0:
            for k in range(0, len(items), 2):
                sumList.append(items[k] + items[k+1])
                result += items[k] + items[k+1]
        else:
            for k in range(0, len(items)-1, 2):
                sumList.append(items[k] + items[k+1])
                result += items[k] + items[k+1]
            sumList.append(items[len(items) -1] )
                    
        items = sumList
        if(len(sumList) < 2):
            break
        
    print(result)