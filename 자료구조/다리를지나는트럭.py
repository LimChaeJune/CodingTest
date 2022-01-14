from collections import deque



def solution(bridge_length, weight, truck_weights):
    answer = 0
    current = 0
   
    wait = deque()
    for truck in truck_weights:
        wait.append(truck)
    queue = deque()            
    done = deque()

    bridge = []

    while len(done) < len(truck_weights):        
        for br in range(len(bridge)):
            bridge[br] -= 1

        if queue and bridge[0] == 0:
            value = queue.popleft()
            done.append(value)
            current -= value
            bridge.remove(0)

        if wait and current + wait[0] <= weight and len(queue) <= bridge_length:
            value = wait.popleft()
            queue.append(value)
            current += value
            bridge.append(bridge_length)       
        

        answer +=1    
        

    return answer

print(solution(100,100, [10,10,10,10,10,10,10,10,10,10]))