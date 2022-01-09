day, cash = map(int,input().split())


dayCashs = []

for _ in range(day):
    dayCashs.append(int(input()))

coins = 0

for i in range(len(dayCashs) - 1):
    currentValue = dayCashs[i]    

    if coins == 0 and currentValue < dayCashs[i+1]:
        coins = cash // currentValue
        cash -= coins * currentValue   
    elif coins > 0:            
        if currentValue > dayCashs[i+1]:
            cash += coins * currentValue
            coins = 0        

if coins > 0:
   cash += coins * dayCashs[len(dayCashs) - 1]
   coins = 0            

print(cash)