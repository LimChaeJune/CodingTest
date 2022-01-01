S = input()

zero = 0
one = 0

before = ''
for i in range(len(S)) :
    if S[i] != before:
        if S[i] == '0': zero += 1
        elif S[i] == '1': one += 1
    before = S[i]

print(min(zero,one))