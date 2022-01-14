s = input()
x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
temp = ''
 
for i in s:
    temp += x[x.index(i)-3]
 
print(temp)