import math
def rounder(x):
    tmp = 1000000 * x
    tmp = math.floor(tmp)
    tmp /= 1000000
    return tmp


arr = []
prod = 1
for cntN in range(4):
    arr.append(int(input()))
    prod *= arr[-1]
su = sum(arr)

print('Sum : {:.6f}'.format( rounder(su)))
print('Average : {:.6f}'.format( rounder(su / 4)))
print('Product : {:.6f}'.format( rounder(prod) ) )
print('MAX : {:.6f}'.format( rounder(max(arr) ) ) )
print('MIN : {:.6f}'.format( rounder(min(arr))))
