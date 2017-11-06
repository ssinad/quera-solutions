a, b, l = [int(x) for x in input().split()]
from math import floor, ceil
print(ceil(l / 2) * a + floor(l / 2) * b)
