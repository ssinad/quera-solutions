n, m = [int(x) for x in input().split()]
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
g = gcd(n, m)
print(g, abs(n * m) // g)
