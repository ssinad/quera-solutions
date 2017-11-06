from math import sqrt, ceil
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for div in range(3, ceil(sqrt(n)) + 1, 2):
        if n % div == 0:
            return False
    return True
a = int(input())
b = int(input())
arr = []
for cnt in range(a, b + 1):
    if isPrime(cnt):
        print(cnt)
