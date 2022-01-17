j, k = map(int, input().split()) 

def gcd(n, m):    
    if n == 0 and m == 0 : return 0

    while True:
        n, m = m ,n % m

        if m == 0:
            break

    return n

def lcm(n, m):    
    if n == 0 and m == 0 : return 0

    result = n * m // gcd(n,m)
    return result

print(gcd(j,k))
print(lcm(j,k))