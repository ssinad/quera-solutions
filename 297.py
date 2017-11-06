x = float(input())
n = int(input())
def expo(x, n):
    num = 1
    den = 1
    sumi = 1
    if n == 1:
        return 1
    for cnt in range(1, n):
        num *= x
        den *= cnt
        sumi += num / den
    return sumi
print("{:.3f}".format(expo(x, n) ))
