import math
def rounder(x):
    tmp = 1000 * x
    tmp = math.floor(tmp)
    tmp /= 1000
    return tmp

n = int(input())
arr = []
for cntN in range(n):
    arr.append(float(input()))
print('Max: {:.3f}'.format( rounder(max(arr))))
print('Min: {:.3f}'.format( rounder(min(arr))))
print('Avg: {:.3f}'.format( rounder(sum(arr) / n)))
