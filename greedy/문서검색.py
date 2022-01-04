doc = input()
search = input()

result = 0
while(len(doc) >= len(search)):
    if doc.find(search) == 0:
        doc = doc[len(search):]
        result += 1
    else :
        doc = doc[1:]


print(result)