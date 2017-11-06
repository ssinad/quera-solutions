import math
n = int(input())
sq = math.ceil(math.sqrt(n))
p = 0
if sq * sq == n:
    p += sq
for i in range(1, sq):
    if n % i == 0:
        p += i
        p += n // i
if p == 2 * n:
    print('YES')
else:
    print('NO')
