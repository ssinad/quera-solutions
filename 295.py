import math
n = int(input())
if n == 0:
    print(1)
else:
    print(1 << math.ceil(math.log2(n)))
