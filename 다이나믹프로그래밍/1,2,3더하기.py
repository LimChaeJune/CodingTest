T = int(input())

items = [1,2,3]

def dpcount(x):
    if(x == 1):
        return 1
    elif(x == 2):
        return 2
    elif(x == 3):
        return 4

    return dpcount(x-1)+dpcount(x-2)+dpcount(x-3)

for _ in range(T):    
    print(dpcount(int(input())))
    