def time_(x, y):
    if x == y:
        if x % 2 == 0:
            return 2 * x
        else:
            return 2 * x - 1
    elif x == y + 2:
        if x % 2 == 0:
            return x + y
        else:
            return x + y - 1 
    else:
        return -1
    
q = int(input())
for cntQ in range(q):
    x, y = [int(tmp) for tmp in input().split()]
    print(time_(x, y))
