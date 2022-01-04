K = input().split('-')

result = 0

for i in range(len(K)):
    if i == 0 : 
        plus = K[i].split('+')
        for pl in plus:
            intValue = int(pl)
            result += intValue
        continue

    minus = K[i].split('+') 
    for m in minus:
        intValue = int(m)
        result -= intValue
        
print(result)