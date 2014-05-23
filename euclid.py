def gcd(n, m):
    s = n % m

    if s == 0:
        return m 
    else:
        n = m
        m = s

    return gcd(n, m)


n = input("n = ")
m = input("m = ")
print gcd(n, m)
