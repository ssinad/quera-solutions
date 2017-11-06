n = int(input())
arr = [int(x) for x in input().split()]
if all(item < 0 for item in arr):
    print(0)
else:
    mx = 0
    su = 0
    for item in arr:
        su += item
        if su < 0:
            su = 0
        if su > mx:
            mx = su
    print(mx)
