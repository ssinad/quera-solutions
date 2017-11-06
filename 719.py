n = int(input())
xs = []
ys = []
for cntN in range(n):
    x, y = [int(tmp) for tmp in input().split()]
    xs.append(x)
    ys.append(y)
xpy = [x + y for x, y in zip(xs, ys)]
x_y = [x - y for x, y in zip(xs, ys)]
l1 = max(xpy) - min(xpy)
l2 = max(x_y) - min(x_y)
print(max(l1, l2))
