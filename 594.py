a, b = [int(x) for x in input().split()]
sum1 = sum2 = 0
i = False
while a != 0:
    c = a % b
    if i:
        sum2 += c
    else:
        sum1 += c
    i = not i
    a //= b
if sum1 == sum2:
    print('Yes')
else:
    print('No')
    
