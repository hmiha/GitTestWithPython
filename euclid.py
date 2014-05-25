def gcd(n, m):
    assert m > 0 and n > 0, "error"
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
