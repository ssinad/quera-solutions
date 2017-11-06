a, b = [int(x) for x in input().split()]
c = abs(b - a)
import math
s = {c}
for div in range(2, math.ceil(math.sqrt(c)) + 1):
    if c % div == 0:
        s.add(div)
        s.add(c // div)
l = list(s)
l.sort()
print(' '.join(str(item) for item in l))
