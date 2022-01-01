Length = int(input())

minus = []
plus = []

result = 0
for _ in range(Length):
    value = int(input())
    if value > 1:
        plus.append(value)
    elif value == 1:
        result += 1
    else:
        minus.append(value)

plus.sort(reverse=True)
minus.sort()

if len(plus) % 2 == 0:
    for i in range(0, len(plus), 2):
        result += plus[i] * plus[i+1]
else :
    for i in range(0, len(plus)-1, 2):
        result += plus[i] * plus[i+1]
    result += plus[len(plus)-1]

if len(minus) % 2 == 0:
    for i in range(0, len(minus), 2):
        result += minus[i] * minus[i+1]
else:
    for i in range(0, len(minus)-1, 2):
        result += minus[i] * minus[i+1]        
    result += minus[len(minus)-1]

print(result)
