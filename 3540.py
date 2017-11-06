n, x, y = [int(x) for x in input().split()]

def num(n, nx, ny):
    global x, y
    if n == 0:
        return (nx, ny)
    if n < 0:
        return -1
    a = num(n - x, nx + 1, ny)
    if a != -1:
        return a
    return num(n -y, nx, ny + 1)

a = num(n, 0, 0)
if a != -1:
    print(a[0], a[1])
else:
    print(a)
