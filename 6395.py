n = int(input())
a = [int(tmp) for tmp in input().split()]
maxi = max(0, a[0])
s = a[0]
for item in a[1:]:
    s += item
    maxi = max(maxi, s)
print(maxi)
